from __future__ import annotations


class Feature(object):

    # Constants to define new level name for range levels
    CURRENT_LEVEL = "Level000"
    CURRENT_VALUE = 0

    def __init__(self, name: str) -> None:
        self.name = name
        self.levels = set()

    def __len__(self) -> int:
        return len(self.levels)

    def get_level(self, min, max):
        for level in self.levels:
            if level.min == min and level.max == max:
                return level

        return None

    def add_level(self, new_level) -> None:

        if not isinstance(new_level, Level):
            print("add_level must receive a Level type")
            raise TypeError

        if new_level.type == "category":
            for level in self.levels:
                if level.type != "category":
                    continue

                # If the new category level is alreay there, do not add.
                # The set structure should be able to solve that, but for some
                # reason I think the hash and eq methods are not working for both
                # ranges and categories.
                if level.name == new_level.name:
                    return

        self.levels.add(new_level)

    def __eq__(self, other: Feature) -> bool:
        return self.name == other.name

    @staticmethod
    def get_new_level() -> str:
        Feature.CURRENT_VALUE += 1
        Feature.CURRENT_LEVEL = Feature.CURRENT_LEVEL[:5] + str(
            Feature.CURRENT_VALUE).zfill(3)

        return Feature.CURRENT_LEVEL


class Level(object):

    TYPES = ["category", "range"]

    def __init__(self, feature: str, type: str, name: str, min: float, max: float) -> None:
        self.name = name
        self.min = min
        self.max = max
        if type not in Level.TYPES:
            print("Level must be 'category' or 'range'.")
            raise TypeError
        self.type = type
        self.feature = feature

    def __hash__(self):
        if self.type == "range":
            return hash(self.feature + str(self.min) + str(self.max))

        if self.type == "category":
            return hash(self.feature + str(self.name))

    def __eq__(self, other: Level) -> bool:

        if self.type == "range" and other.type == "range":
            if self.feature == other.feature and \
                abs(self.min - other.min) < 0.0001 and \
                    abs(self.max - other.max) < 0.0001:
                return True
            else:
                return False

        if self.type == "cateogry" and other.type == "category":
            return self.name == other.name

        print("Comparing levels of different types")
        raise TypeError

    def __str__(self) -> str:
        result = f"Feature: {self.name}\n"
        result += f"Name: {self.name}\n"
        result += f"Type: {self.type}\n"
        if self.type == "category":
            result += f"Value: {self.min}"
        else:
            result += f"Range: ({self.min}, {self.max})"

        return result

    def short_str(self) -> str:
        return f"{self.name}: ({self.min}, {self.max})"
