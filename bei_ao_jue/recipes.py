from general.recipes import DamageRecipe, CriticalRecipe


RECIPES = {
    "雷走风切": [
        "雷走风切(5%伤害)", "雷走风切(4%伤害)", "雷走风切(4%会心)", "雷走风切(3%伤害)", "雷走风切(3%会心)", "雷走风切(2%会心)"
    ],
    "上将军印": [
        "上将军印(4%伤害)", "上将军印(4%会心)", "上将军印(3%伤害)", "上将军印(3%会心)", "上将军印(2%伤害)", "上将军印(2%会心)"
    ],
    "破釜沉舟": [
        "破釜沉舟(5%伤害)", "破釜沉舟(4%伤害)", "破釜沉舟(4%会心)", "破釜沉舟(3%伤害)", "破釜沉舟(3%会心)", "破釜沉舟(2%会心)"
    ],
    "擒龙六斩": [
        "擒龙六斩(5%伤害)", "擒龙六斩(4%伤害)", "擒龙六斩(4%会心)", "擒龙六斩(3%伤害)", "擒龙六斩(3%会心)", "擒龙六斩(2%会心)"
    ],
    "刀啸风吟": [
        "刀啸风吟(5%伤害)", "刀啸风吟(4%伤害)", "刀啸风吟(4%会心)", "刀啸风吟(3%会心)", "刀啸风吟(2%会心)"
    ],
}
RECIPE_GAINS = {
    "雷走风切(5%伤害)": DamageRecipe(["雷走风切"], 0.05),
    "雷走风切(4%伤害)": DamageRecipe(["雷走风切"], 0.04),
    "雷走风切(4%会心)": CriticalRecipe(["雷走风切"], 0.04),
    "雷走风切(3%伤害)": DamageRecipe(["雷走风切"], 0.03),
    "雷走风切(3%会心)": CriticalRecipe(["雷走风切"], 0.03),
    "雷走风切(2%会心)": CriticalRecipe(["雷走风切"], 0.02),

    "上将军印(4%伤害)": DamageRecipe(["上将军印"], 0.04),
    "上将军印(4%会心)": CriticalRecipe(["上将军印"], 0.04),
    "上将军印(3%伤害)": DamageRecipe(["上将军印"], 0.03),
    "上将军印(3%会心)": CriticalRecipe(["上将军印"], 0.03),
    "上将军印(2%伤害)": DamageRecipe(["上将军印"], 0.02),
    "上将军印(2%会心)": CriticalRecipe(["上将军印"], 0.02),

    "破釜沉舟(5%伤害)": DamageRecipe(["破釜沉舟"], 0.05),
    "破釜沉舟(4%伤害)": DamageRecipe(["破釜沉舟"], 0.04),
    "破釜沉舟(4%会心)": CriticalRecipe(["破釜沉舟"], 0.04),
    "破釜沉舟(3%会心)": CriticalRecipe(["破釜沉舟"], 0.03),
    "破釜沉舟(3%伤害)": DamageRecipe(["破釜沉舟"], 0.03),
    "破釜沉舟(2%会心)": CriticalRecipe(["破釜沉舟"], 0.02),

    "擒龙六斩(5%伤害)": DamageRecipe(["惊燕式", "逐鹰式"], 0.05),
    "擒龙六斩(4%伤害)": DamageRecipe(["惊燕式", "逐鹰式"], 0.04),
    "擒龙六斩(4%会心)": CriticalRecipe(["惊燕式", "逐鹰式"], 0.04),
    "擒龙六斩(3%伤害)": DamageRecipe(["惊燕式", "逐鹰式"], 0.03),
    "擒龙六斩(3%会心)": CriticalRecipe(["惊燕式", "逐鹰式"], 0.03),
    "擒龙六斩(2%会心)": CriticalRecipe(["惊燕式", "逐鹰式"], 0.02),
    
    "刀啸风吟(5%伤害)": DamageRecipe(["刀啸风吟"], 0.05),
    "刀啸风吟(4%伤害)": DamageRecipe(["刀啸风吟"], 0.04),
    "刀啸风吟(4%会心)": CriticalRecipe(["刀啸风吟"], 0.04),
    "刀啸风吟(3%会心)": CriticalRecipe(["刀啸风吟"], 0.03),
    "刀啸风吟(2%会心)": CriticalRecipe(["刀啸风吟"], 0.02),
}