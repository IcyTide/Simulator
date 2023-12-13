import re

from base.constant import FRAME_PER_SECOND


class Comparison:
    def __init__(self, operator, number):
        self.number = number
        if operator == ">":
            self.comparison = self.gt_comparison
        elif operator == "<":
            self.comparison = self.lt_comparison
        elif operator == ">=":
            self.comparison = self.ge_comparison
        elif operator == "<=":
            self.comparison = self.le_comparison
        elif operator == "=":
            self.comparison = self.eq_comparison
        else:
            self.comparison = self.ne_comparison

    def gt_comparison(self, number):
        return number > self.number

    def lt_comparison(self, number):
        return number < self.number

    def ge_comparison(self, number):
        return number >= self.number

    def le_comparison(self, number):
        return number <= self.number

    def eq_comparison(self, number):
        return number == self.number

    def ne_comparison(self, number):
        return number == self.number

    def __call__(self, number):
        return self.comparison(number)


class Condition:
    def __init__(self, entity, condition, operator, number, status):
        self.entity = entity
        if condition == "cd":
            self.condition = self.cd_condition
            number = int(number * FRAME_PER_SECOND)
            self.gcd_index = status.skills[entity].gcd_index
        elif condition == "energy":
            self.condition = self.energy_condition
        elif condition == "duration":
            self.condition = self.duration_condition
            number = int(number * FRAME_PER_SECOND)
        else:
            self.condition = self.stack_condition
        self.comparison = Comparison(operator, number)

    def cd_condition(self, status):
        return max(status.gcd_group.get(self.gcd_index, 0), status.cds.get(self.entity, 0))

    def energy_condition(self, status):
        return status.energies[self.entity]

    def duration_condition(self, status):
        return status.durations.get(self.entity, 0)

    def stack_condition(self, status):
        return status.stacks[self.entity]

    def __call__(self, status):
        return self.comparison(self.condition(status))


class Aggregation:
    def __init__(self, condition1, condition2, operator):
        self.condition1 = condition1
        self.condition2 = condition2
        if operator == "&":
            self.aggregation = self.and_aggregation
        else:
            self.aggregation = self.or_aggregation

    def and_aggregation(self, status):
        return self.condition1(status) and self.condition2(status)

    def or_aggregation(self, status):
        return self.condition1(status) or self.condition2(status)

    def __call__(self, status):
        return self.aggregation(status)


def empty_condition(*args, **kwargs):
    return True


def parse_condition(status, text):
    full_pattern = r"([\u4e00-\u9fa5·0-9a-zA-Z]+)\(?(.*)\)?"
    condition_pattern = r"([\u4e00-\u9fa50-9a-zA-Z·-]+):?(\w+)([<>=!]+)(\d+)"
    logic_pattern = r"[&|]"
    operators = [">", "<", "=", "!=", ">=", "<="]

    full_matches = re.match(full_pattern, text)
    if not full_matches:
        raise SyntaxError

    skill, conditions = full_matches.group(1), full_matches.group(2)
    if skill not in status.skills:
        raise SyntaxError

    final_condition = None
    if conditions:
        logic_operators = re.findall(logic_pattern, conditions)
        for condition in re.split(logic_pattern, conditions):
            condition_matches = re.match(condition_pattern, condition)

            comparison_operator = condition_matches.group(3)
            if comparison_operator not in operators:
                raise SyntaxError

            number = float(condition_matches.group(4))
            if number < 0:
                raise SyntaxError

            entity = condition_matches.group(1)
            target = condition_matches.group(2)
            if target in ["cd", "energy"]:
                if entity not in status.skills:
                    raise SyntaxError
            elif target in ["duration", "stack"]:
                if entity not in status.buffs:
                    raise SyntaxError
            else:
                raise SyntaxError

            if final_condition:
                final_condition = Aggregation(
                    final_condition, Condition(entity, target, comparison_operator, number, status), logic_operators.pop(0)
                )
            else:
                final_condition = Condition(entity, target, comparison_operator, number, status)

    if not final_condition:
        final_condition = empty_condition

    return status.skills[skill], final_condition


def parse_expression(status, text):
    return [parse_condition(status, sub) for sub in re.split(r"\s*,\s*", text)]
