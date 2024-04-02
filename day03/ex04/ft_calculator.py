class calculator:

    @staticmethod
    def dotproduct(V1: list[float], V2: list[float]) -> None:
        final_res = 0
        res = [V1[i] * V2[i] for i in range(0, len(V1))]
        for v in res:
            final_res += v
        print("Dot product is:", final_res)

    @staticmethod
    def add_vec(V1: list[float], V2: list[float]) -> None:
        res = [float(V1[i] + V2[i]) for i in range(0, len(V1))]
        print("Add Vector is:", res)

    @staticmethod
    def sous_vec(V1: list[float], V2: list[float]) -> None:
        res = [float(V1[i] - V2[i]) for i in range(0, len(V1))]
        print("Sous Vector is:", res)
