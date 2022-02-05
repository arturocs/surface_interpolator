pub struct F3DPoint {
    x: f32,
    y: f32,
    z: f32,
}
//trait BezierSurface {
//    fn decasteljau_surfaces(points: &[2DPoint]) -> &[2DPoint]
//    fn degree_elevation(points: &[2DPoint], degree: i32) -> &[2DPoint]
//    fn interpolant_surfaces(left: f32, right: f32, step_long: f32, function: String) -> &[3DPoint]
// easy on the surfaces one, there is a lot of things to define first
//}

fn Vij(i: f32, j: f32, h: f32) -> (f32, f32) {
    return (i * h + j * h, i * h - j * h);
}

fn uij11(i: f32, j: f32, h: f32) -> (f32, f32) {
    let vij = Vij(i, j, h);
    let vij1 = Vij(i + 1.0, j + 1.0, h);
    return ((3.0 * vij.0 + vij1.0) / 4.0, (3.0 * vij.1 + vij1.1) / 4.0);
}

fn uij10(i: f32, j: f32, h: f32) -> (f32, f32) {
    let vij = Vij(i, j, h);
    let vij1 = Vij(i + 1.0, j, h);
    return ((3.0 * vij.0 + vij1.0) / 4.0, (3.0 * vij.1 + vij1.1) / 4.0);
}

fn uij0minus1(i: f32, j: f32, h: f32) -> (f32, f32) {
    let vij = Vij(i, j, h);
    let vij1 = Vij(i, j - 1.0, h);
    return ((3.0 * vij.0 + vij1.0) / 4.0, (3.0 * vij.1 + vij1.1) / 4.0);
}
fn uijminus1minus1(i: f32, j: f32, h: f32) -> (f32, f32) {
    let vij = Vij(i, j, h);
    let vij1 = Vij(i - 1.0, j - 1.0, h);
    return ((3.0 * vij.0 + vij1.0) / 4.0, (3.0 * vij.1 + vij1.1) / 4.0);
}
fn uijminus10(i: f32, j: f32, h: f32) -> (f32, f32) {
    let vij = Vij(i, j, h);
    let vij1 = Vij(i - 1.0, j, h);
    return ((3.0 * vij.0 + vij1.0) / 4.0, (3.0 * vij.1 + vij1.1) / 4.0);
}
fn uij01(i: f32, j: f32, h: f32) -> (f32, f32) {
    let vij = Vij(i, j, h);
    let vij1 = Vij(i, j + 1.0, h);
    return ((3.0 * vij.0 + vij1.0) / 4.0, (3.0 * vij.1 + vij1.1) / 4.0);
}

fn eij10(i: f32, j: f32, h: f32) -> (f32, f32) {
    let vij = Vij(i, j, h);
    let vij1 = Vij(i + 1.0, j, h);
    return ((vij.0 + vij1.0) / 2.0, (vij.1 + vij1.1) / 2.0);
}

fn eij11(i: f32, j: f32, h: f32) -> (f32, f32) {
    let vij = Vij(i, j, h);
    let vij1 = Vij(i + 1.0, j + 1.0, h);
    return ((vij.0 + vij1.0) / 2.0, (vij.1 + vij1.1) / 2.0);
}
fn eij01(i: f32, j: f32, h: f32) -> (f32, f32) {
    let vij = Vij(i, j, h);
    let vij1 = Vij(i, j + 1.0, h);
    return ((vij.0 + vij1.0) / 2.0, (vij.1 + vij1.1) / 2.0);
}

fn zij11(i: f32, j: f32, h: f32) -> (f32, f32) {
    let vij = Vij(i, j, h);
    let vij1 = Vij(i + 1.0, j + 1.0, h);
    let vij2 = Vij(i + 1.0, j, h);
    return (
        (2.0 * vij.0 + vij1.0 + vij2.0) / 4.0,
        (2.0 * vij.1 + vij1.1 + vij2.1) / 4.0,
    );
}
fn zij10(i: f32, j: f32, h: f32) -> (f32, f32) {
    let vij = Vij(i, j, h);
    let vij1 = Vij(i + 1.0, j, h);
    let vij2 = Vij(i, j - 1.0, h);
    return (
        (2.0 * vij.0 + vij1.0 + vij2.0) / 4.0,
        (2.0 * vij.1 + vij1.1 + vij2.1) / 4.0,
    );
}
fn zij0minus1(i: f32, j: f32, h: f32) -> (f32, f32) {
    let vij = Vij(i, j, h);
    let vij1 = Vij(i, j - 1.0, h);
    let vij2 = Vij(i - 1.0, j - 1.0, h);
    return (
        (2.0 * vij.0 + vij1.0 + vij2.0) / 4.0,
        (2.0 * vij.1 + vij1.1 + vij2.1) / 4.0,
    );
}
fn zijminus1minus1(i: f32, j: f32, h: f32) -> (f32, f32) {
    let vij = Vij(i, j, h);
    let vij1 = Vij(i - 1.0, j - 1.0, h);
    let vij2 = Vij(i - 1.0, j, h);
    return (
        (2.0 * vij.0 + vij1.0 + vij2.0) / 4.0,
        (2.0 * vij.1 + vij1.1 + vij2.1) / 4.0,
    );
}
fn zijminus10(i: f32, j: f32, h: f32) -> (f32, f32) {
    let vij = Vij(i, j, h);
    let vij1 = Vij(i - 1.0, j, h);
    let vij2 = Vij(i, j + 1.0, h);
    return (
        (2.0 * vij.0 + vij1.0 + vij2.0) / 4.0,
        (2.0 * vij.1 + vij1.1 + vij2.1) / 4.0,
    );
}
fn zij01(i: f32, j: f32, h: f32) -> (f32, f32) {
    let vij = Vij(i, j, h);
    let vij1 = Vij(i, j + 1.0, h);
    let vij2 = Vij(i + 1.0, j + 1.0, h);
    return (
        (2.0 * vij.0 + vij1.0 + vij2.0) / 4.0,
        (2.0 * vij.1 + vij1.1 + vij2.1) / 4.0,
    );
}
fn tij(i: f32, j: f32, h: f32) -> (f32, f32) {
    let vij = Vij(i, j, h);
    let vij1 = Vij(i + 1.0, j + 1.0, h);
    let vij2 = Vij(i + 1.0, j, h);
    return (
        (vij.0 + vij1.0 + vij2.0) / 3.0,
        (vij.1 + vij1.1 + vij2.1) / 3.0,
    );
}
fn bij(i: f32, j: f32, h: f32) -> (f32, f32) {
    let vij = Vij(i, j, h);
    let vij1 = Vij(i + 1.0, j + 1.0, h);
    let vij2 = Vij(i, j + 1.0, h);
    return (
        (vij.0 + vij1.0 + vij2.0) / 3.0,
        (vij.1 + vij1.1 + vij2.1) / 3.0,
    );
}
fn wij11(i: f32, j: f32, h: f32) -> (f32, f32) {
    let vij = Vij(i, j, h);
    let vij1 = Vij(i + 1.0, j + 1.0, h);
    return ((2.0 * vij.0 + vij1.0) / 3.0, (2.0 * vij.1 + vij1.1) / 3.0);
}
fn wij10(i: f32, j: f32, h: f32) -> (f32, f32) {
    let vij = Vij(i, j, h);
    let vij1 = Vij(i + 1.0, j, h);
    return ((2.0 * vij.0 + vij1.0) / 3.0, (2.0 * vij.1 + vij1.1) / 3.0);
}
fn wij0minus1(i: f32, j: f32, h: f32) -> (f32, f32) {
    let vij = Vij(i, j, h);
    let vij1 = Vij(i, j - 1.0, h);
    return ((2.0 * vij.0 + vij1.0) / 3.0, (2.0 * vij.1 + vij1.1) / 3.0);
}
fn wijminus1minus1(i: f32, j: f32, h: f32) -> (f32, f32) {
    let vij = Vij(i, j, h);
    let vij1 = Vij(i - 1.0, j - 1.0, h);
    return ((2.0 * vij.0 + vij1.0) / 3.0, (2.0 * vij.1 + vij1.1) / 3.0);
}
fn wijminus10(i: f32, j: f32, h: f32) -> (f32, f32) {
    let vij = Vij(i, j, h);
    let vij1 = Vij(i - 1.0, j, h);
    return ((2.0 * vij.0 + vij1.0) / 3.0, (2.0 * vij.1 + vij1.1) / 3.0);
}
fn wij01(i: f32, j: f32, h: f32) -> (f32, f32) {
    let vij = Vij(i, j, h);
    let vij1 = Vij(i, j + 1.0, h);
    return ((2.0 * vij.0 + vij1.0) / 3.0, (2.0 * vij.1 + vij1.1) / 3.0);
}
