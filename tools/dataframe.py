from typing import Union, List, Any, Dict


class Series:
    index: List[Union[int, str]]
    data: List[Any]

    def __init__(self, data=None, index=None):
        if data is None:
            self.data = []
        else:
            self.data = data
        if index is None:
            self.index = []
        else:
            self.index = index

        assert len(self.data) == len(self.index)

    def __len__(self):
        return len(self.data)

    def __repr__(self):
        return "\n".join([f"{i}:\t{d}" for i, d in zip(self.index, self.data)])

    def __getitem__(self, key):
        if isinstance(key, (list, tuple)):
            assert all(isinstance(k, bool) for k in key)
            assert len(self.data) == len(key)
            index, data = [], []
            for i, k in enumerate(key):
                if not k:
                    continue
                index.append(self.index[i])
                data.append(self.data[i])
            return Series(data, index)
        if key in self.index:
            return self.data[self.index.index(key)]
        raise IndexError(f"{key} not in index")

    def __setitem__(self, key, value):
        if isinstance(key, (list, tuple)):
            assert all(isinstance(k, bool) for k in key)
            assert len(self.data) == len(key)
            for i, k in enumerate(key):
                if not k:
                    continue
                self.data[i] = value
        elif key in self.index:
            self.data[key] = value
        else:
            self.index.append(key)
            self.data.append(value)

    def remove(self, index):
        i = self.index.index(index)
        self.data.pop(i)
        self.index.pop(i)

    def __bool__(self):
        return bool(self.data)

    def __iter__(self):
        for e in self.data:
            yield e

    def items(self):
        for i, d in zip(self.index, self.data):
            yield i, d

    def __and__(self, value):
        if isinstance(value, Series):
            assert self.index == value.index
            return Series([d and v for d, v in zip(self, value)], self.index)
        return Series([d and value for d in self.data], self.index)

    def __or__(self, value):
        if isinstance(value, Series):
            assert self.index == value.index
            return Series([d or v for d, v in zip(self, value)], self.index)
        return Series([d or value for d in self.data], self.index)

    def __eq__(self, value):
        return Series([d == value for d in self.data], self.index)

    def __gt__(self, value):
        return Series([d > value for d in self.data], self.index)

    def __lt__(self, value):
        return Series([d < value for d in self.data], self.index)

    def __ge__(self, value):
        return Series([d >= value for d in self.data], self.index)

    def __le__(self, value):
        return Series([d <= value for d in self.data], self.index)

    def __ne__(self, value):
        return Series([d != value for d in self.data], self.index)

    def __add__(self, value):
        return Series([d + value for d in self.data], self.index)

    def __sub__(self, value):
        return Series([d - value for d in self.data], self.index)

    def __mul__(self, value):
        return Series([d * value for d in self.data], self.index)

    def __truediv__(self, value):
        return Series([d / value for d in self.data], self.index)

    def __iadd__(self, value):
        self.data = [d + value for d in self.data]
        return self

    def __isub__(self, value):
        self.data = [d - value for d in self.data]
        return self

    def __imul__(self, value):
        self.data = [d * value for d in self.data]
        return self

    def __itruediv__(self, value):
        self.data = [d / value for d in self.data]
        return self


class DataFrame:
    index: int = 0
    columns: List[str]
    data: Dict[str, Series]

    def __init__(self, data: Dict[str, Series]=None, index: int=0, columns: List[str]=None):
        self.index = index
        if data:
            self.data = data
            self.columns = list(self.data)
        else:
            assert columns
            self.columns = columns
            self.data = {c: Series() for c in self.columns}

    def __repr__(self):
        content = "\t" + "\t".join(self.columns)
        for i in self.indexes:
            row = f"{i}"
            for c in self.columns:
                row += f"\t{self.data[c][i]}"
            content += f"\n{row}"
        return content

    def __getitem__(self, key):
        if isinstance(key, str):
            return self.data[key]
        elif isinstance(key, int):
            return Series([self.data[c][key] for c in self.columns], self.columns)
        elif isinstance(key, Series):
            assert len(self.indexes) == len(key)
            frame_data = {}
            for c in self.columns:
                index, series_data = [], []
                for i, k in key.items():
                    if not k:
                        continue
                    index.append(i)
                    series_data.append(self.data[c][i])
                frame_data[c] = Series(series_data, index)
            return DataFrame(frame_data, self.index)

    def __getattr__(self, name):
        if name in self.columns:
            return self[name]
        raise AttributeError(f"DataFrame has not attribute {name}")

    def append(self, item):
        assert len(item) == len(self.columns)
        
        for c, e in zip(self.columns, item):
            self.data[c][self.index] = e
        self.index += 1

    def remove(self, index):
        if isinstance(index, Series):
            for k, v in index.items():
                if not v:
                    continue
                self.remove(k)
        else:
            for c in self.columns:
                self.data[c].remove(index)

    @property
    def indexes(self):
        indexes = []
        for i in range(self.index):
            for c in self.columns:
                if i not in self.data[c].index:
                    break
            else:
                indexes.append(i)
        return indexes

if __name__ == '__main__':
    df = DataFrame(columns=["a", "b", "c", "d"])
    print(df)

    df.append([1, 2, 3, (1, 2)])
    df.append([4, 5, 6, (1, 2)])
    df.append([7, 8, 9, (1, 2)])
    print("\n添加新行后:")
    print(df)

    df.remove(2)
    print("\n移除索引为2的行后:")
    print(df)

    df.append([7, 8, 9, (1, 2)])
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
