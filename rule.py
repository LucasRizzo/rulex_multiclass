from __future__ import annotations
import pandas as pd

class Rule(object):

    def __init__(self, index: float, rule_str: str="", weight: float=None, conditions: list=None) -> None:
        self.rule_str = rule_str
        self.weight = weight

        if conditions is None:
            self.conditions = []
        else:
            self.conditions = conditions
        
        self.index = index

    def __eq__(self, other: Rule) -> bool:
        if self.weight is not None and other.weight is not None:
            return self.rule_str == other.rule_str and abs(self.weight - other.weight) < 0.00001
        elif self.weight is None and other.weight is None:
            return self.rule_str == other.rule_str
        else:
            return False

    def __str__(self) -> str:
        result = f"Rule: {self.rule_str}"
        if self.weight is not None:
            result += f", Weight: {self.weight}"
        else:
            result += ", Weight: None"
        
        return result
    
    def get_rule_str(self, rules_df: pd.core.frame.DataFrame, conclusion_set: list) -> str:
        rule = ""
        features_full = list()  # List of features used
        for premise in self.conditions:
            # Append all features used so it is possible count their frequency
            features_full.append(premise.feature)

        features_set = set(features_full)  # Unique features employed

        for feature in features_set:

            total = features_full.count(feature)

            if total == 1:  # If feature has been used only once it ends with " AND "
                for premise in self.conditions:
                    if premise.feature == feature:
                        rule += f"\"{premise.name} {premise.feature}\" AND "
                        break
            else:  # If feature has been used more than once,
                # it needs to concatenate all possibilities with " OR "
                rule += f"("
                for premise in self.conditions:
                    if premise.feature == feature:
                        rule += f"\"{premise.name} {premise.feature}\" OR "
                # Remove last " OR " and add new " AND "
                rule = rule[:-4] + ") AND "

        rule = rule[:-5]  # Remove last " AND "
        output_value = rules_df.loc[self.index, "Output value"]

        for conclusion in conclusion_set:
            if conclusion[0] == output_value:
                rule += f" -> {conclusion[0]
                               } [{conclusion[1]}, {conclusion[2]}]"
                break
            else:
                print(conclusion[0], output_value)

        return rule
    
    def get_rule_str(self, rules_df: pd.core.frame.DataFrame, conclusion_set: list) -> str:
        rule = ""
        features_full = list()  # List of features used
        for premise in self.conditions:
            # Append all features used so it is possible count their frequency
            features_full.append(premise.feature)

        features_set = set(features_full)  # Unique features employed

        for feature in features_set:

            total = features_full.count(feature)

            if total == 1:  # If feature has been used only once it ends with " AND "
                for premise in self.conditions:
                    if premise.feature == feature:
                        rule += f"\"{premise.name} {premise.feature}\" AND "
                        break
            else:  # If feature has been used more than once,
                # it needs to concatenate all possibilities with " OR "
                rule += f"("
                for premise in self.conditions:
                    if premise.feature == feature:
                        rule += f"\"{premise.name} {premise.feature}\" OR "
                # Remove last " OR " and add new " AND "
                rule = rule[:-4] + ") AND "

        rule = rule[:-5]  # Remove last " AND "
        try:
            output_value = rules_df.loc[self.index, "Output value"]
        except KeyError:
            print("Output value not found")
            print(rules_df.loc[self.index,])
            input("Pause...")

        for conclusion in conclusion_set:
            if conclusion[0] == output_value:
                rule += f" -> {conclusion[0]
                               } [{conclusion[1]}, {conclusion[2]}]"
                break
           
        return rule

