# Simulator

A pure-python based simulator for Monte Carlo simulation in JX3

## How to deploy

All simulator codes are pure-python and using some features in latest python version.

So, please make sure run in python>=3.9

```
  // clone repository
  git clone git@github.com:IcyTide/Simulator.git

  // cd working directory
  cd Simulator

  // install gradio package for UI support
  pip install -r requirements.txt

  // start application
  python ui/app.py
```
After above steps, your default browser will pop out to show the ui
## Attribute - 属性基类
代码位置：Simulator/base/attribute
### Major Attribute - 主属性
目前影响DPS的包含身法、力道、根骨、元气四种主属性，本节需要涉及以下Constant常量
- AGILITY_TO_CRITICAL_STRIKE-身法转换会心: $655 / 1024 = 0.6396484375$<a id="AGILITY_TO_CRITICAL"></a>
- STRENGTH_TO_ATTACK_POWER-力道转换攻击: $153 / 1024 = 0.1494140625$<a id="STRENGTH_TO_ATTACK"></a>
- STRENGTH_TO_OVERCOME-力道转换破防: $307 / 1024 = 0.2998046875$<a id="STRENGTH_TO_OVERCOME"></a>
- SPIRIT_TO_CRITICAL_STRIKE-根骨转换会心: $655 / 1024 = 0.6396484375$<a id="SPIRIT_TO_CRITICAL"></a>
- SPUNK_TO_ATTACK_POWER-元气转换攻击: $184 / 1024 = 0.1796875$<a id="SPUNK_TO_ATTACK"></a>
- SPUNK_TO_OVERCOME-元气转换破防: $307 / 1024 = 0.2998046875$<a id="SPUNK_TO_OVERCOME"></a>
#### Agility - 身法
影响身法数值的有以下两部分:
- agility_base-基础身法：通过装备、消耗品和部分BUFF获得的具体身法数值
- agility_gain-身法增益: 通过奇穴、阵眼和部分BUFF获得的百分比身法增益
  
最终身法数值由以下公式推导得：
$$
    agility=agility\_base + INT(agility\_base \times agility\_gain)
$$
其中$agility$为面板身法，$INT$为Floor取整(非四舍五入，直接抹除小数)

通过公式可以看出身法增益对于基础身法是乘法增益，且面板身法为一个整数值
<br><br><br>

此外，身法会影响外功会心的数值(外功会心等级)，比例为$655 / 1024 = 0.6396484375$

$$
    base\_physical\_critical\_strike=INT(physical\_critical_strike\_base + agility \times AGILITY\_TO\_CRITICAL\_STRIKE + extra\_physical\_critical\_strike)
$$
其中$base\_physical\_critical\_strike$，$physical\_critical_strike\_base$和$extra\_physical\_critical\_strike$见[下文](#PHYSICAL_CRITICAL)，$agility \times AGILITY\_TO\_CRITICAL\_STRIKE$为身法带来的**额外**外功会心等级，$AGILITY\_TO\_CRITICAL\_STRIKE$为[此处](#AGILITY_TO_CRITICAL)引入的常量值
<br><br><br>

以下为agility相关的属性代码
```python
    @property
    def agility_base(self):
        return self._agility_base

    @agility_base.setter
    def agility_base(self, agility_base):
        self._agility_base = agility_base
        self.agility = agility_base * (1 + self._agility_gain)

    @property
    def agility_gain(self):
        return self._agility_gain

    @agility_gain.setter
    def agility_gain(self, agility_gain):
        self._agility_gain = agility_gain
        self.agility = self._agility_base * (1 + agility_gain)

    @property
    def agility(self):
        return self._agility

    @agility.setter
    def agility(self, agility):
        agility = INT(agility)
        self._agility = agility
        self.base_physical_critical_strike = (self._physical_critical_strike_base + self._extra_physical_critical_strike
                                              + agility * AGILITY_TO_CRITICAL_STRIKE)
```

#### Strength-力道
影响力道数值的有以下两部分:
- strength_base-基础力道: 通过装备、消耗品和部分BUFF获得的具体力道数值
- strength_gain-力道增益: 通过奇穴、阵眼和部分BUFF获得的百分比力道增益

最终力道数值由以下公式推导得：
$$
    strength=strength\_base + INT(strength\_base \times strength\_gain)
$$
其中$strength$为面板力道，$INT$为Floor取整(非四舍五入，直接抹除小数)

通过公式可以看出力道增益对于基础力道是乘法增益，且面板力道为一个整数值。
<br><br><br>

<a id="STRENGTH_ATTACK_POWER"></a>此外，力道会影响外功攻击的数值(基础外功攻击)，比例为$153 / 1024 = 0.1494140625$
$$
    base\_physical\_attack\_power=physical\_attack\_power\_base + INT(strength \times STRENGTH\_TO\_ATTACK\_POWER)
$$
其中$base\_physical\_attack\_power$和$physical\_attack\_power\_base$见[下文](#PHYSICAL_ATTACK_POWER)，$INT(strength \times STRENGTH\_TO\_ATTACK\_POWER)$为力道带来的**额外**基础外功攻击，$STRENGTH\_TO\_ATTACK\_POWER$为[此处](#STRENGTH_TO_ATTACK)引入的常量值
<br><br><br>

力道还会影响外功破防的数值(基础外功破防)，比例为$307 / 1024 = 0.2998046875$
$$
    base\_physical\_overcome=physical\_overcome\_base + INT(strength \times STRENGTH\_TO\_OVERCOME)
$$
其中$base\_physical\_overcome$和$physical\_overcome\_base$见[下文](#PHYSICAL_OVERCOME)，$INT(strength \times STRENGTH\_TO\_OVERCOME)$为力道带来的额外基础外功破防，$STRENGTH\_TO\_OVERCOME$为[此处](#STRENGTH_TO_OVERCOME)引入的常量值
<br><br><br>

以下为strength相关的属性代码
```python
    @property
    def strength_base(self):
        return self._strength_base

    @strength_base.setter
    def strength_base(self, strength_base):
        self._strength_base = strength_base
        self.strength = strength_base * (1 + self._strength_gain)

    @property
    def strength_gain(self):
        return self._strength_gain

    @strength_gain.setter
    def strength_gain(self, strength_gain):
        self._strength_gain = strength_gain
        self.strength = self._strength_base * (1 + strength_gain)

    @property
    def strength(self):
        return self._strength

    @strength.setter
    def strength(self, strength):
        strength = INT(strength)
        self._strength = strength
        self.base_physical_attack_power = self._physical_attack_power_base + strength * STRENGTH_TO_ATTACK_POWER
        self.base_physical_overcome = self._physical_overcome_base + strength * STRENGTH_TO_OVERCOME
```

#### Spirit - 根骨
影响根骨数值的有以下两部分:
- spirit\_base-基础根骨: 通过装备、消耗品和部分BUFF获得的具体根骨数值
- spirit\_gain-根骨增益: 通过奇穴、阵眼和部分BUFF获得的百分比根骨增益
最终根骨数值由以下公式推导得：
$$
    spirit=spirit\_base + INT(spirit\_base \times spirit\_gain)
$$
其中$spirit$为面板根骨，$INT$为Floor取整(非四舍五入，直接抹除小数)。

通过公式可以看出根骨增益对于基础根骨是乘法增益，且面板根骨为一个整数值。
<br><br><br>

此外，根骨会影响内功会心的数值(内功会心等级)，比例为$655 / 1024 = 0.6396484375$
$$
    base\_magical\_critical_strike=INT(magical\_critical_strike\_base + spirit \times SPIRIT\_TO\_CRITICAL_STRIKE + extra\_magical\_critical\_strike)
$$
其中$base\_magical\_critical_strike$，$magical\_critical_strike\_base$和$extra\_magical\_critical\_strike$见[下文](#MAGICAL_CRITICAL)，$spirit \times SPIRIT\_TO\_CRITICAL_STRIKE$为根骨带来的**额外**内功会心等级，$SPIRIT\_TO\_CRITICAL\_STRIKE$为[此处](#SPIRIT_TO_CRITICAL)
<br><br><br>

以下为spirit相关的属性代码
```python
        @property
    def spirit_base(self):
        return self._spirit_base

    @spirit_base.setter
    def spirit_base(self, spirit_base):
        self._spirit_base = spirit_base
        self.spirit = spirit_base * (1 + self._spirit_gain)

    @property
    def spirit_gain(self):
        return self._spirit_gain

    @spirit_gain.setter
    def spirit_gain(self, spirit_gain):
        self._spirit_gain = spirit_gain
        self.spirit = self._spirit_base * (1 + spirit_gain)

    @property
    def spirit(self):
        return self._spirit

    @spirit.setter
    def spirit(self, spirit):
        spirit = INT(spirit)
        self._spirit = spirit
        self.base_magical_critical_strike = (self._magical_critical_strike_base + self._extra_magical_critical_strike
                                             + spirit * SPIRIT_TO_CRITICAL_STRIKE)
```

#### Spunk-元气
影响元气数值的有以下两部分:
- spunk_base-基础元气: 通过装备、消耗品和部分BUFF获得的具体元气数值
- spunk_gain-元气增益: 通过奇穴、阵眼和部分BUFF获得的百分比元气增益

最终元气数值由以下公式推导得：
$$
    spunk=spunk\_base + INT(spunk\_base \times spunk\_gain)
$$
其中$spunk$为面板元气，$INT$为Floor取整(非四舍五入，直接抹除小数)

通过公式可以看出元气增益对于基础元气是乘法增益，且面板元气为一个整数值。
<br><br><br>

<a id="SPUNK_ATTACK_POWER"></a>此外，元气会影响内功攻击的数值(基础内功攻击)，比例为$184 / 1024 = 0.1796875$
$$
    base\_magical\_attack\_power=magical\_attack\_power\_base + INT(spunk \times SPUNK\_TO\_ATTACK\_POWER)
$$
其中$base\_magical\_attack\_power$和$magical\_attack\_power\_base$见[下文](#MAGIC_ATTACK_POWER)，$INT(spunk \times SPUNK\_TO\_ATTACK\_POWER)$为元气带来的**额外**基础内功攻击，SPUNK_TO_ATTACK_POWER为[此处](#SPUNK_TO_ATTACK)引入的常量值
<br><br><br>

元气还会影响内功破防的数值(基础内功破防)，比例为$307 / 1024 = 0.2998046875$
$$
    base\_magical\_overcome=base\_magical\_overcome + INT(spunk \times SPUNK\_TO\_OVERCOME)
$$
其中$base\_magical\_overcome$和$magical\_overcome\_base$见[下文](#MAGICAL_OVERCOME)，$INT(spunk \times SPUNK\_TO\_OVERCOME)$为元气带来的额外基础内功破防，SPUNK_TO_OVERCOME为[此处](#SPUNK_TO_OVERCOME)引入的常量值
<br><br><br>

以下为spunk相关的属性代码
```python
    @property
    def spunk_base(self):
        return self._spunk_base

    @spunk_base.setter
    def spunk_base(self, spunk_base):
        self._spunk_base = spunk_base
        self.spunk = spunk_base * (1 + self._spunk_gain)

    @property
    def spunk_gain(self):
        return self._spunk_gain

    @spunk_gain.setter
    def spunk_gain(self, spunk_gain):
        self._spunk_gain = spunk_gain
        self.spunk = self._spunk_base * (1 + spunk_gain)

    @property
    def spunk(self):
        return self._spunk

    @spunk.setter
    def spunk(self, spunk):
        spunk = INT(spunk)
        self._spunk = spunk
        self.base_magical_attack_power = self._magical_attack_power_base + spunk * SPUNK_TO_ATTACK_POWER
        self.base_magical_overcome = self._magical_overcome_base + spunk * SPUNK_TO_OVERCOME
```

##### All Major-全属性
全属性实际指**全部主属性**，基础全属性和全属性增益均全部作用于四种主属性，规则相同，代码实现该部分作为包装后的调用入口
```python
    @property
    def all_major_base(self):
        return self._all_major_base

    @all_major_base.setter
    def all_major_base(self, all_major_base):
        residual = all_major_base - self._all_major_base
        self.agility_base += residual
        self.strength_base += residual
        self.spirit_base += residual
        self.spunk_base += residual
        self._all_major_base = all_major_base

    @property
    def all_major_gain(self):
        return self._all_major_gain

    @all_major_gain.setter
    def all_major_gain(self, all_major_gain):
        residual = all_major_gain - self._all_major_gain
        self.agility_gain += residual
        self.strength_gain += residual
        self.spirit_gain += residual
        self.spunk_gain += residual
        self._all_major_gain = all_major_gain
```

##### Extra Attribute By Major-心法带来的主属性额外加成
注意！！！心法带来的主属性额外加成往往是加在“最终”部分的，并不能和以上主属性加成一概而论，对于这部分请详见下方各属性


### Coficient Attribute - 系数属性
#### Attack Power-攻击
这里的攻击力暂时分为外功攻击和内功攻击，对于特定类型（阴性、阳性、毒性、混元）攻击可以视为内功攻击或者单独实现

##### Physical Attack Power-外功攻击
影响外功攻击的部分由以下三部分组成
- physical_attack_power_base-基础外功攻击：通过心法、装备、消耗品和部分BUFF获得的具体外功攻击数值
- physical_attack_power_gain-外功攻击增益：通过奇穴、阵眼和部分BUFF获得的百分比外功攻击增益
- extra_physical_attack_power-额外外功攻击：通过心法属性获得的主属性转换额外攻击

面板基础外功攻击由以下公式推导得：
$$
base\_physical\_attack\_power=physical\_attack\_power\_base + INT(strength \times STRENGTH\_TO\_ATTACK\_POWER)
$$
<a id="PHYSICAL_ATTACK_POWER"></a>其中$base\_physical\_attack\_power$为面板基础外功攻击，$INT(strength \times STRENGTH\_TO\_ATTACK\_POWER)$见[上文](#STRENGTH_ATTACK_POWER)

通过公式可以看出面板基础外功攻击为一个整数值。

最终外功攻击由以下公式推导得
$$
physical\_attack\_power=base\_physical\_attack\_power + INT(base\_physical\_attack\_power \times physical\_attack\_power\_gain) +extra\_physical\_attack\_power
$$
其中$physical\_attack\_power$为面板最终外功攻击，$INT$为Floor取整(非四舍五入，直接抹除小数)

通过公式可以看出外功攻击增益对于基础外功攻击是乘法增益，心法带来的额外攻击力并不受外功攻击增益影响，且最终外功攻击为一个整数值

##### Magical Attack Power-内功攻击
影响内功攻击的部分由以下三部分组成
- magical_attack_power_base-基础内功攻击：通过心法、装备、消耗品和部分BUFF获得的具体基础内功攻击数值
- magical_attack_power_base-内功攻击增益：通过奇穴、阵眼和部分BUFF获得的百分比内功攻击增益
- extra_magical_attack_power-额外内功攻击：通过心法属性获得的主属性转换额外攻击

面板基础内功攻击由以下公式推导得：
$$
base\_magical\_attack\_power=magical\_attack\_power\_base + INT(strength \times STRENGTH\_TO\_ATTACK\_POWER)
$$
<a id="MAGICAL_ATTACK_POWER"></a>其中$base\_magical\_attack\_power$为面板基础内功攻击，$INT(spunk \times SPUNK\_TO\_ATTACK\_POWER)$见[上文](#SPUNK_ATTACK_POWER)

通过公式可以看出面板基础内功攻击为一个整数值。

最终内功攻击由以下公式推导得
$$
magical\_attack\_power=base\_magical\_attack\_power + INT(base\_magical\_attack\_power \times magical\_attack\_power\_gain) +extra\_magical\_attack\_power
$$
其中$magical\_attack\_power$为面板最终内功攻击，$INT$为Floor取整(非四舍五入，直接抹除小数)

通过公式可以看出内功攻击增益对于基础内功攻击是乘法增益，心法带来的额外攻击力并不受内功攻击增益影响，且最终内功攻击为一个整数值


### Minor Attribute - 副属性
目前影响DPS的包含破防、会心、会心效果、破招、无双、加速六种副属性，本节需要涉及以下Constant常量
- CRITICAL_STRIKE_SCALE-会心百分比缩放：$78622.5$<a id="CRITICAL-STRIKE_SCALE"></a>
- OVERCOME_SCALE-破防百分比缩放: $78622.5$<a id="OVERCOME_SCALE"></a>
#### Overcome-破防
这里的破防暂时分为外功破防和内功破防，对于特定类型（阴性、阳性、毒性、混元）破防可以视为内功破防或者单独实现
##### Physical Attack Power-外功破防
影响外功破防的部分由以下三部分组成
- physical_overcome_base-基础外功破防：通过心法、装备、消耗品和部分BUFF获得的具体外功破防数值
- physical_overcome_gain-外功破防增益：通过奇穴、阵眼和部分BUFF获得的百分比外功破防增益
- extra_physical_overcome-额外外功破防：通过心法属性获得的主属性转换额外破防

面板基础外功破防由以下公式推导得：
$$
base\_physical\_overcome=physical\_overcome\_base + INT(strength \times STRENGTH\_TO\_OVERCOME)
$$
<a id="PHYSICAL_OVERCOME"></a>其中$base\_physical\_overcome$为面板基础外功破防，$INT(strength \times STRENGTH\_TO\_OVERCOME)$见[上文](#STRENGTH_OVERCOME)

通过公式可以看出面板基础外功破防为一个整数值。

最终外功破防由以下公式推导得
$$
final\_physical\_overcome=INT(base\_physical\_overcome + base\_physical\_overcome \times physical\_overcome\_gain +extra\_physical\_overcome)
$$
其中$final\_physical\_overcome$为面板最终外功破防，$INT$为Floor取整(非四舍五入，直接抹除小数)

通过公式可以看出外功破防增益对于基础外功破防是乘法增益，心法带来的额外破防力并不受外功破防增益影响，且最终外功破防为一个整数值。

外功破防百分比由以下公式推导得
$$
physical\_overcome=final\_physical\_overcome \ OVERCOME_SCALE
$$
其中$physical\_overcome$为面板最终外功破防

通过公式可以看出外功破防百分比是一个小数

##### Magical Attack Power-内功破防
影响内功破防的部分由以下三部分组成
- magical_overcome_base-基础内功破防：通过心法、装备、消耗品和部分BUFF获得的具体基础内功破防数值
- magical_overcome_base-内功破防增益：通过奇穴、阵眼和部分BUFF获得的百分比内功破防增益
- extra_magical_overcome-额外内功破防：通过心法属性获得的主属性转换额外破防

面板基础内功破防由以下公式推导得：
$$
base\_magical\_overcome=magical\_overcome\_base + INT(strength \times STRENGTH\_TO\_OVERCOME)
$$
<a id="MAGICAL_OVERCOME"></a>其中$base\_magical\_overcome$为面板基础内功破防，$INT(spunk \times SPUNK\_TO\_OVERCOME)$见[上文](#SPUNK_OVERCOME)

通过公式可以看出面板基础内功破防为一个整数值。

最终内功破防由以下公式推导得
$$
final\_magical\_overcome=INT(base\_magical\_overcome + base\_magical\_overcome \times magical\_overcome\_gain + extra\_magical\_overcome)
$$
其中$final\_magical\_overcome$为面板最终内功破防，$INT$为Floor取整(非四舍五入，直接抹除小数)

通过公式可以看出内功破防增益对于基础内功破防是乘法增益，心法带来的额外破防力并不受内功破防增益影响，且最终内功破防为一个整数值

内功破防百分比由以下公式推导得
$$
magical\_overcome=final\_magical\_overcome \ OVERCOME_SCALE
$$
其中$magical\_overcome$为面板最终外功破防

通过公式可以看出内功破防百分比是一个小数

#### Critical Strike-会心
这里的会心暂时分为外功会心和内功会心，对于特定类型（阴性、阳性、毒性、混元）会心可以视为内功会心或者单独实现
##### Physical Attack Power-外功会心
影响外功会心的部分由以下三部分组成
- physical_critical_strike_base-基础外功会心：通过心法、装备、消耗品和部分BUFF获得的具体外功会心数值
- physical_critical_strike_gain-外功会心增益：通过奇穴、阵眼和部分BUFF获得的百分比外功会心增益
- extra_physical_critical_strike-额外外功会心：通过心法属性获得的主属性转换额外会心

外功会心等级由以下公式推导得：
$$
base\_physical\_critical_strike=INT(physical\_critical_strike\_base + agility \times AGILITY\_TO\_CRITICAL_STRIKE + extra_physical_critical_strike)
$$
<a id="PHYSICAL_CRITICAL"></a>其中$base\_physical\_critical_strike$为外功会心等级，$INT(agility \times AGILITY\_TO\_CRITICAL_STRIKE)$见[上文](#AGILITY_CRITICAL)

通过公式可以看出外功会心等级为一个整数值。

外功会心百分比由以下公式推导得
$$
physical\_critical_strike=base\_physical\_critical_strike / CRITICAL_STRIKE_SCALE + physical\_critical\_strike\_gain
$$
其中$physical\_critical_strike$为面板最终外功会心，$INT$为Floor取整(非四舍五入，直接抹除小数)

通过公式可以看出外功会心增益对于外功会心百分比是加法增益，心法带来的额外会心并不受外功会心增益影响，且最终外功会心为一个小数

##### Magical Attack Power-内功会心
影响内功会心的部分由以下三部分组成
- magical_critical_strike_base-基础内功会心：通过心法、装备、消耗品和部分BUFF获得的具体内功会心数值
- magical_critical_strike_gain-内功会心增益：通过奇穴、阵眼和部分BUFF获得的百分比内功会心增益
- extra_magical_critical_strike-额外内功会心：通过心法属性获得的主属性转换额外会心

内功会心等级由以下公式推导得：
$$
base\_magical\_critical_strike=INT(magical\_critical_strike\_base + spirit \times SPIRIT\_TO\_CRITICAL_STRIKE + extra_magical_critical_strike)
$$
<a id="PHYSICAL_CRITICAL"></a>其中$base\_magical\_critical_strike$为内功会心等级，$INT(spirit \times SPIRIT\_TO\_CRITICAL_STRIKE)$见[上文](#SPIRIT_CRITICAL)

通过公式可以看出内功会心等级为一个整数值。

内功会心百分比由以下公式推导得
$$
magical\_critical_strike=base\_magical\_critical_strike / CRITICAL_STRIKE_SCALE + magical\_critical\_strike\_gain
$$
其中$magical\_critical_strike$为面板最终内功会心，$INT$为Floor取整(非四舍五入，直接抹除小数)

通过公式可以看出内功会心增益对于内功会心百分比是加法增益，心法带来的额外会心并不受内功会心增益影响，且最终内功会心为一个小数
