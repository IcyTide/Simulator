from typing import Dict, List


class Series:
    rows: Dict[int, object]
    column: str

    def __init__(self, rows, column=None):
        self.rows = rows
        self.column = column

    def __len__(self):
        return len(self.rows)

    def __repr__(self):
        return "\n".join([f"{i}:\t{getattr(d, self.column)}" for i, d in self.rows.items()])

    def items(self):
        if not self.column:
            return self.rows.items()
        return [(i, getattr(d, self.column)) for i, d in self.rows.items()]

    def __getitem__(self, key):
        if key in self.rows:
            if not self.column:
                return self.rows[key]
            else:
                return getattr(self.rows[key], self.column)
        raise IndexError(f"{key} not in index")

    def __setitem__(self, key, value):
        for v in self.rows.values():
            setattr(v, self.column, value)

    def __bool__(self):
        return bool(self.rows)

    def __and__(self, value):
        if isinstance(value, Series):
            return Series({i: d and value[i] for i, d in self.items()})
        return Series({i: d and value for i, d in self.items()})

    def __or__(self, value):
        if isinstance(value, Series):
            return Series({i: d or value[i] for i, d in self.items()})
        return Series({i: d or value for i, d in self.items()})

    def __eq__(self, value):
        return Series({i: d == value for i, d in self.items()})

    def __lt__(self, other):
        return Series({i: d < other for i, d in self.items()})

    def __gt__(self, other):
        return Series({i: d > other for i, d in self.items()})

    def __le__(self, other):
        return Series({i: d <= other for i, d in self.items()})

    def __ge__(self, other):
        return Series({i: d >= other for i, d in self.items()})

    def __add__(self, value):
        for v in self.rows.values():
            setattr(v, self.column, getattr(v, self.column) + value)
        return self

    def __iadd__(self, value):
        return self + value

    def __sub__(self, value):
        for v in self.rows.values():
            setattr(v, self.column, getattr(v, self.column) - value)
        return self

    def __isub__(self, value):
        return self - value


class DataFrame:
    _index: int = 0
    columns: List[str]
    rows: Dict[int, object]

    def __init__(
            self, columns: List[str], rows: Dict[int, object] = None, index: int = 0
    ):
        self.columns = columns
        if rows:
            self.rows = rows
        else:
            self.rows = {}
        self._index = index

    def __repr__(self):
        content = "," + ",".join(self.columns)
        for i, row in self.rows.items():
            sub_content = f"{i}"
            for c in self.columns:
                sub_content += f",{getattr(row, c)}"
            content += f"\n{sub_content}"
        return content

    def __getitem__(self, key):
        if isinstance(key, str):  # get column data
            return Series(self.rows, key)
        elif isinstance(key, int):  # get row data
            return self.rows[key]
        elif isinstance(key, Series):
            assert len(self.rows) == len(key)
            rows = {}
            for i, k in key.items():
                if not k:
                    continue
                rows[i] = self.rows[i]
            return DataFrame(self.columns, rows, self._index)
        else:
            assert False

    def __setitem__(self, key, value):
        if isinstance(key, str):
            for v in self.rows.values():
                setattr(v, key, value)
        elif isinstance(key, int):
            self.rows[key] = value
        elif isinstance(key, Series):
            for i, k in key.rows.items():
                if not k:
                    continue
                self.rows[i] = value

    def __getattr__(self, name):
        if name in self.columns:
            return self[name]
        raise AttributeError(f"DataFrame has not attribute {name}")

    def __iter__(self):
        for i in self.rows:
            yield self.rows[i]

    def append(self, item):
        if not item.index:
            item.index = self._index
            self._index += 1
        self.rows[item.index] = item
        return item.index

    def remove(self, index):
        return self.rows.pop(index)

    def first(self):
        return list(self.rows.values())[0]

    def last(self):
        return list(self.rows.values())[-1]

    def __bool__(self):
        if self.rows:
            return True
        else:
            return False


if __name__ == '__main__':
    df = DataFrame(columns=["a", "b", "c", "d"])
    print(df)


    class Inst:
        def __init__(self, a, b, c, d):
            self.a = a
            self.b = b
            self.c = c
            self.d = d


    df.append(Inst(1, 2, 3, (1, 2)))
    df.append(Inst(4, 5, 6, (1, 2)))
    df.append(Inst(7, 8, 9, (1, 2)))
    print("\n添加新行后:")
    print(df)

    df.remove(2)
    print("\n移除索引为2的行后:")
    print(df)

    df.append(Inst(7, 8, 9, (1, 2)))
    print("\n添加新行后:")
    print(df)

    print("\n索引为1的行")
    print(df[1])
    print("\na列")
    print(df['a'])

    cond_1 = df.a > 1
    print("cond1筛选结果:")
    print(cond_1)

    cond_2 = df.c < 7
    print("cond2筛选结果:")
    print(cond_2)

    print("cond筛选结果:")
    print(df[cond_1 & cond_2])

    df.b += 4
    print("b列加4后:")
    print(df)

    # 使用remove方法
    df.remove(cond_1 & cond_2)
    print("\n移除某些行后:")
    print(df)
