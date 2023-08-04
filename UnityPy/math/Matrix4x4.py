from .Vector3 import Vector3


class Matrix4x4:
    M: list

    def __init__(self, values):
        if len(values) != 16:
            raise ValueError(
                "There must be sixteen and only sixteen input values for Matrix."
            )
        self.M = values

    def __getitem__(self, index):
        if isinstance(index, tuple):
            index = index[0] + index[1] * 4
        return self.M[index]

    def __setitem__(self, index, value):
        if isinstance(index, tuple):
            # row, column
            index = index[0] + index[1] * 4
        self.M[index] = value

    def __eq__(self, other):
        if not isinstance(other, Matrix4x4):
            return False
        print()

    def __mul__(self, rhs):
        res = Matrix4x4([0] * 16)
        res.M00 = (
            (self.M00 * rhs.M00 + self.M01 * rhs.M10) + self.M02 * rhs.M20
        ) + self.M03 * rhs.M30
        res.M01 = (
            (self.M00 * rhs.M01 + self.M01 * rhs.M11) + self.M02 * rhs.M21
        ) + self.M03 * rhs.M31
        res.M02 = (
            (self.M00 * rhs.M02 + self.M01 * rhs.M12) + self.M02 * rhs.M22
        ) + self.M03 * rhs.M32
        res.M03 = (
            (self.M00 * rhs.M03 + self.M01 * rhs.M13) + self.M02 * rhs.M23
        ) + self.M03 * rhs.M33

        res.M10 = (
            (self.M10 * rhs.M00 + self.M11 * rhs.M10) + self.M12 * rhs.M20
        ) + self.M13 * rhs.M30
        res.M11 = (
            (self.M10 * rhs.M01 + self.M11 * rhs.M11) + self.M12 * rhs.M21
        ) + self.M13 * rhs.M31
        res.M12 = (
            (self.M10 * rhs.M02 + self.M11 * rhs.M12) + self.M12 * rhs.M22
        ) + self.M13 * rhs.M32
        res.M13 = (
            (self.M10 * rhs.M03 + self.M11 * rhs.M13) + self.M12 * rhs.M23
        ) + self.M13 * rhs.M33

        res.M20 = (
            (self.M20 * rhs.M00 + self.M21 * rhs.M10) + self.M22 * rhs.M20
        ) + self.M23 * rhs.M30
        res.M21 = (
            (self.M20 * rhs.M01 + self.M21 * rhs.M11) + self.M22 * rhs.M21
        ) + self.M23 * rhs.M31
        res.M22 = (
            (self.M20 * rhs.M02 + self.M21 * rhs.M12) + self.M22 * rhs.M22
        ) + self.M23 * rhs.M32
        res.M23 = (
            (self.M20 * rhs.M03 + self.M21 * rhs.M13) + self.M22 * rhs.M23
        ) + self.M23 * rhs.M33

        res.M30 = (
            (self.M30 * rhs.M00 + self.M31 * rhs.M10) + self.M32 * rhs.M20
        ) + self.M33 * rhs.M30
        res.M31 = (
            (self.M30 * rhs.M01 + self.M31 * rhs.M11) + self.M32 * rhs.M21
        ) + self.M33 * rhs.M31
        res.M32 = (
            (self.M30 * rhs.M02 + self.M31 * rhs.M12) + self.M32 * rhs.M22
        ) + self.M33 * rhs.M32
        res.M33 = (
            (self.M30 * rhs.M03 + self.M31 * rhs.M13) + self.M32 * rhs.M23
        ) + self.M33 * rhs.M33

        return res

    @staticmethod
    def Scale(vector: Vector3):
        return Matrix4x4(
            [vector.X, 0, 0, 0, 0, vector.Y, 0, 0, 0, 0, vector.Z, 0, 0, 0, 0, 1]
        )

    @property
    def M00(self):
        return self.M[0]

    @M00.setter
    def M00(self, value):
        self.M[0] = value

    @property
    def M10(self):
        return self.M[1]

    @M10.setter
    def M10(self, value):
        self.M[1] = value

    @property
    def M20(self):
        return self.M[2]

    @M20.setter
    def M20(self, value):
        self.M[2] = value

    @property
    def M30(self):
        return self.M[3]

    @M30.setter
    def M30(self, value):
        self.M[3] = value

    @property
    def M01(self):
        return self.M[4]

    @M01.setter
    def M01(self, value):
        self.M[4] = value

    @property
    def M11(self):
        return self.M[5]

    @M11.setter
    def M11(self, value):
        self.M[5] = value

    @property
    def M21(self):
        return self.M[6]

    @M21.setter
    def M21(self, value):
        self.M[6] = value

    @property
    def M31(self):
        return self.M[7]

    @M31.setter
    def M31(self, value):
        self.M[7] = value

    @property
    def M02(self):
        return self.M[8]

    @M02.setter
    def M02(self, value):
        self.M[8] = value

    @property
    def M12(self):
        return self.M[9]

    @M12.setter
    def M12(self, value):
        self.M[9] = value

    @property
    def M22(self):
        return self.M[10]

    @M22.setter
    def M22(self, value):
        self.M[10] = value

    @property
    def M32(self):
        return self.M[11]

    @M32.setter
    def M32(self, value):
        self.M[11] = value

    @property
    def M03(self):
        return self.M[12]

    @M03.setter
    def M03(self, value):
        self.M[12] = value

    @property
    def M13(self):
        return self.M[13]

    @M13.setter
    def M13(self, value):
        self.M[13] = value

    @property
    def M23(self):
        return self.M[14]

    @M23.setter
    def M23(self, value):
        self.M[14] = value

    @property
    def M33(self):
        return self.M[15]

    @M33.setter
    def M33(self, value):
        self.M[15] = value
