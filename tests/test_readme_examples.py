"""Keep the Python usage examples in the README executable."""

import re
from pathlib import Path


def test_readme_python_examples():
    """Run the documented usage examples together in their displayed order."""
    readme = (Path(__file__).parents[1] / "README.md").read_text(encoding="utf-8")
    blocks = re.findall(r"```python\n(.*?)```", readme, re.DOTALL)
    assert blocks, "README has no Python examples"
    namespace = {}
    for block in blocks:
        exec(compile(block, "README.md", "exec"), namespace)


def test_documented_mutation_behavior():
    """Inherited append mutates; overridden sort and reverse leave the input alone."""
    from listo import listo

    values = listo(3, 1, 2)
    assert values.append(4) is None
    assert values == [3, 1, 2, 4]
    assert values.sort() == [1, 2, 3, 4]
    assert values.reverse() == [4, 2, 1, 3]
    assert values == [3, 1, 2, 4]


def test_documented_single_iterable_behavior():
    """Generators unpack, while legacy sequences not registered as Iterable do not."""
    from listo import listo

    class LegacySequence:
        def __getitem__(self, index):
            if index == 0:
                return 42
            raise IndexError

    legacy = LegacySequence()
    assert list(legacy) == [42]
    assert listo(legacy) == [legacy]
    assert listo(x for x in (1, 2)) == [1, 2]
