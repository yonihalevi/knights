from logic import *

AKnight = Symbol("A is a Knight")
AKnave = Symbol("A is a Knave")

BKnight = Symbol("B is a Knight")
BKnave = Symbol("B is a Knave")

CKnight = Symbol("C is a Knight")
CKnave = Symbol("C is a Knave")

# Puzzle 0
# A says "I am both a knight and a knave."
knowledge0 = And(
    Or(AKnight, AKnave),
    Implication(AKnight, Not(AKnave)),
    Implication(AKnave, Not(AKnight)),
    Implication(AKnight, And(AKnight, AKnave)),
)


# Puzzle 1
# A says "We are both knaves."
# B says nothing.
knowledge1 = And(
    #general rules for A and B
    Or(AKnight, AKnave),
    Implication(AKnight, Not(AKnave)),
    Implication(AKnave, Not(AKnight)),
    Or(BKnight, BKnave),
    Implication(BKnight, Not(BKnave)),
    Implication(BKnave, Not(BKnight)),

    #implication of the statment by A
    Implication(AKnight, And(AKnave, BKnave)),
    Implication(AKnave, Or( AKnight, BKnight)),
)

# Puzzle 2
# A says "We are the same kind."
# B says "We are of different kinds."
knowledge2 = And(
    #general rules for A and B
    Or(AKnight, AKnave),
    Implication(AKnight, Not(AKnave)),
    Implication(AKnave, Not(AKnight)),
    Or(BKnight, BKnave),

    #implications of both statements
    Implication(AKnight, BKnight),
    Implication(AKnave, Not(BKnave)),
    Implication(BKnight, AKnave),
    Implication(BKnave, Not(AKnight)),
)

# Puzzle 3
# A says either "I am a knight." or "I am a knave.", but you don't know which.
# B says "A said 'I am a knave'."
# B says "C is a knave."
# C says "A is a knight."
knowledge3 = And(
    # general rules for A, B and C
    # general rules for A and B
    Or(AKnight, AKnave),
    Implication(AKnight, Not(AKnave)),
    Implication(AKnave, Not(AKnight)),
    Or(BKnight, BKnave),
    Implication(BKnight, Not(BKnave)),
    Implication(BKnave, Not(BKnight)),
    Or(CKnight, CKnave),
    Implication(CKnight, Not(CKnave)),
    Implication(CKnave, Not(CKnight)),

    #implication of C's statement
    Implication(CKnight, AKnight),
    Implication(CKnave, AKnave),

    #implication of B's statements
    Implication(BKnight, CKnave),
    Implication(BKnight, And(Implication(AKnave, Not(AKnave)), Implication(AKnight, AKnave))),
    Implication(BKnave, And(Implication(AKnight, AKnight), Implication(AKnave, Not(AKnave)))),

)


def main():
    symbols = [AKnight, AKnave, BKnight, BKnave, CKnight, CKnave]
    puzzles = [
        ("Puzzle 0", knowledge0),
        ("Puzzle 1", knowledge1),
        ("Puzzle 2", knowledge2),
        ("Puzzle 3", knowledge3)
    ]
    for puzzle, knowledge in puzzles:
        print(puzzle)
        if len(knowledge.conjuncts) == 0:
            print("    Not yet implemented.")
        else:
            for symbol in symbols:
                if model_check(knowledge, symbol):
                    print(f"    {symbol}")


if __name__ == "__main__":
    main()
