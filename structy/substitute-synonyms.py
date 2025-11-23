import unittest


# time:  O(nmⁿ)
# space: O(nmⁿ)
# where: n = number of words in sentence, m = max number of synonyms for a word
def substitute_synonyms(sentence: str, synonyms: dict[str, list[str]]) -> list[str]:
    result: list[str] = []
    words = sentence.split()

    def _backtrack(idx: int) -> None:
        if idx == len(words):
            result.append(" ".join(words))
            return

        if (original := words[idx]) in synonyms:
            for synonym in synonyms[original]:
                words[idx] = synonym
                _backtrack(idx + 1)
                words[idx] = original
        else:
            _backtrack(idx + 1)

    _backtrack(0)
    return result


class TestSolution(unittest.TestCase):
    def test_00(self) -> None:
        sentence = "follow the yellow brick road"
        synonyms = {"follow": ["chase", "pursue"], "yellow": ["gold", "amber", "lemon"]}
        self.assertCountEqual(
            substitute_synonyms(sentence, synonyms),
            [
                "chase the gold brick road",
                "chase the amber brick road",
                "chase the lemon brick road",
                "pursue the gold brick road",
                "pursue the amber brick road",
                "pursue the lemon brick road",
            ],
        )

    def test_01(self) -> None:
        sentence = "I think it's gonna be a long long time"
        synonyms = {"think": ["believe", "reckon"], "long": ["lengthy", "prolonged"]}
        self.assertCountEqual(
            substitute_synonyms(sentence, synonyms),
            [
                "I believe it's gonna be a lengthy lengthy time",
                "I believe it's gonna be a lengthy prolonged time",
                "I believe it's gonna be a prolonged lengthy time",
                "I believe it's gonna be a prolonged prolonged time",
                "I reckon it's gonna be a lengthy lengthy time",
                "I reckon it's gonna be a lengthy prolonged time",
                "I reckon it's gonna be a prolonged lengthy time",
                "I reckon it's gonna be a prolonged prolonged time",
            ],
        )

    def test_02(self) -> None:
        sentence = "palms sweaty knees weak arms heavy"
        synonyms = {
            "palms": ["hands", "fists"],
            "heavy": ["weighty", "hefty", "burdensome"],
            "weak": ["fragile", "feeble", "frail", "sickly"],
        }
        self.assertCountEqual(
            substitute_synonyms(sentence, synonyms),
            [
                "hands sweaty knees fragile arms weighty",
                "hands sweaty knees fragile arms hefty",
                "hands sweaty knees fragile arms burdensome",
                "hands sweaty knees feeble arms weighty",
                "hands sweaty knees feeble arms hefty",
                "hands sweaty knees feeble arms burdensome",
                "hands sweaty knees frail arms weighty",
                "hands sweaty knees frail arms hefty",
                "hands sweaty knees frail arms burdensome",
                "hands sweaty knees sickly arms weighty",
                "hands sweaty knees sickly arms hefty",
                "hands sweaty knees sickly arms burdensome",
                "fists sweaty knees fragile arms weighty",
                "fists sweaty knees fragile arms hefty",
                "fists sweaty knees fragile arms burdensome",
                "fists sweaty knees feeble arms weighty",
                "fists sweaty knees feeble arms hefty",
                "fists sweaty knees feeble arms burdensome",
                "fists sweaty knees frail arms weighty",
                "fists sweaty knees frail arms hefty",
                "fists sweaty knees frail arms burdensome",
                "fists sweaty knees sickly arms weighty",
                "fists sweaty knees sickly arms hefty",
                "fists sweaty knees sickly arms burdensome",
            ],
        )


if __name__ == "__main__":
    unittest.main()
