from UnityPy.classes import Mesh


def export_mesh(m_Mesh: Mesh, format="obj") -> str:
    if format == "obj":
        return export_mesh_obj(m_Mesh)
    raise NotImplementedError(f"Export format {format} not implemented")


def export_mesh_obj(m_Mesh, material_names: list = None):
    if m_Mesh.m_VertexCount <= 0:
        return False

    sb = [f"g {m_Mesh.name}\r\n"]
    if material_names:
        sb.append(f"mtllib {m_Mesh.name}.mtl\r\n")
    # region Vertices
    if not m_Mesh.m_Vertices:
        return False

    c = 4 if len(m_Mesh.m_Vertices) == m_Mesh.m_VertexCount * 4 else 3
    sb.extend(
        "v {0:.7G} {1:.7G} {2:.7G}\r\n".format(
            -m_Mesh.m_Vertices[v * c],
            m_Mesh.m_Vertices[v * c + 1],
            m_Mesh.m_Vertices[v * c + 2],
        ).replace("nan", "0")
        for v in range(int(m_Mesh.m_VertexCount))
    )
    # endregion

    # region UV
    if m_Mesh.m_UV0:
        if len(m_Mesh.m_UV0) == m_Mesh.m_VertexCount * 2:
            c = 2
        elif len(m_Mesh.m_UV0) == m_Mesh.m_VertexCount * 3:
            c = 3

        sb.extend(
            "vt {0:.7G} {1:.7G}\r\n".format(
                m_Mesh.m_UV0[v * c], m_Mesh.m_UV0[v * c + 1]
            ).replace("nan", "0")
            for v in range(int(m_Mesh.m_VertexCount))
        )
    # endregion

    # region Normals
    if m_Mesh.m_Normals:
        if len(m_Mesh.m_Normals) == m_Mesh.m_VertexCount * 3:
            c = 3
        elif len(m_Mesh.m_Normals) == m_Mesh.m_VertexCount * 4:
            c = 4

        sb.extend(
            "vn {0:.7G} {1:.7G} {2:.7G}\r\n".format(
                -m_Mesh.m_Normals[v * c],
                m_Mesh.m_Normals[v * c + 1],
                m_Mesh.m_Normals[v * c + 2],
            ).replace("nan", "0")
            for v in range(int(m_Mesh.m_VertexCount))
        )
    # endregion

    # region Face
    sum = 0
    for i in range(len(m_Mesh.m_SubMeshes)):
        sb.append(f"g {m_Mesh.name}_{i}\r\n")
        if material_names and i < len(material_names) and material_names[i]:
            sb.append(f"usemtl {material_names[i]}\r\n")
        indexCount = m_Mesh.m_SubMeshes[i].indexCount
        end = sum + indexCount // 3
        sb.extend(
            "f {0}/{0}/{0} {1}/{1}/{1} {2}/{2}/{2}\r\n".format(
                m_Mesh.m_Indices[f * 3 + 2] + 1,
                m_Mesh.m_Indices[f * 3 + 1] + 1,
                m_Mesh.m_Indices[f * 3] + 1,
            )
            for f in range(sum, end)
        )
        sum = end
    # endregion
    return "".join(sb)
