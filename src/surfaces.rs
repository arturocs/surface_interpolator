struct F3DPoint {
    x: f32,
    y: f32,
    z: f32
}
//trait BezierSurface {
//    fn decasteljau_surfaces(points: &[2DPoint]) -> &[2DPoint]
//    fn degree_elevation(points: &[2DPoint], degree: i32) -> &[2DPoint]
//    fn interpolant_surfaces(left: f32, right: f32, step_long: f32, function: String) -> &[3DPoint]
    // easy on the surfaces one, there is a lot of things to define first
//}

fn Vij(i: i8, j: i8, h: f32) -> (f32,f32) {
    return (i*h + j*h, i*h-j*h)
}

fn uij11(i: i8, j: i8, h: f32) -> (f32,f32) {
    let vij = Vij(i,j,h);
    let vij1 = Vij(i+1, j+1, h);
    return ( (3*vij.0 + vij1.0) / 4, (3*vij.1 + vij1.1) / 4 )
}

fn uij10(i: i8, j: i8, h: f32) -> (f32,f32) {
    let vij = Vij(i,j,h);
    let vij1 = Vij(i+1, j, h);
    return ( (3*vij.0 + vij1.0) / 4, (3*vij.1 + vij1.1) / 4 )
}

fn uij0minus1(i: i8, j: i8, h: f32) -> (f32,f32) {
    let vij = Vij(i,j,h);
    let vij1 = Vij(i, j-1, h);
    return ( (3*vij.0 + vij1.0) / 4, (3*vij.1 + vij1.1) / 4 )
}
fn uijminus1minus1(i: i8, j: i8, h: f32) -> (f32,f32) {
    let vij = Vij(i,j,h);
    let vij1 = Vij(i-1, j-1, h);
    return ( (3*vij.0 + vij1.0) / 4, (3*vij.1 + vij1.1) / 4 )
}
fn uijminus10(i: i8, j: i8, h: f32) -> (f32,f32) {
    let vij = Vij(i,j,h);
    let vij1 = Vij(i-1, j, h);
    return ( (3*vij.0 + vij1.0) / 4, (3*vij.1 + vij1.1) / 4 )
}
fn uij01(i: i8, j: i8, h: f32) -> (f32,f32) {
    let vij = Vij(i,j,h);
    let vij1 = Vij(i, j+1, h);
    return ( (3*vij.0 + vij1.0) / 4, (3*vij.1 + vij1.1) / 4 )
}

fn eij10(i: i8, j: i8, h: f32) -> (f32,f32) {
    let vij = Vij(i,j,h);
    let vij1 = Vij(i+1, j, h);
    return ( (vij.0 + vij1.0) / 2, (vij.1 + vij1.1) / 2 )
}
fn eij11(i: i8, j: i8, h: f32) -> (f32,f32) {
    let vij = Vij(i,j,h);
    let vij1 = Vij(i+1, j+1, h);
    return ( (vij.0 + vij1.0) / 2, (vij.1 + vij1.1) / 2 )
}
fn eij01(i: i8, j: i8, h: f32) -> (f32,f32) {
    let vij = Vij(i,j,h);
    let vij1 = Vij(i, j+1, h);
    return ( (vij.0 + vij1.0) / 2, (vij.1 + vij1.1) / 2 )
}
fn eij10(i: i8, j: i8, h: f32) -> (f32,f32) {
    let vij = Vij(i,j,h);
    let vij1 = Vij(i+1, j, h);
    return ( (vij.0 + vij1.0) / 2, (vij.1 + vij1.1) / 2 )
}
fn zij11(i: i8, j: i8, h: f32) -> (f32,f32) {
    let vij = Vij(i,j,h);
    let vij1 = Vij(i+1, j+1, h);
    let vij2 = Vij(i+1, j, h);
    return ( (2*vij.0+vij1.0+vij2.0)/4,(2*vij.1+vij1.1+vij2.1)/4 )
}
fn zij10(i: i8, j: i8, h: f32) -> (f32,f32) {
    let vij = Vij(i,j,h);
    let vij1 = Vij(i+1, j, h);
    let vij2 = Vij(i, j-1, h);
    return ( (2*vij.0+vij1.0+vij2.0)/4,(2*vij.1+vij1.1+vij2.1)/4 )
}
fn zij0minus1(i: i8, j: i8, h: f32) -> (f32,f32) {
    let vij = Vij(i,j,h);
    let vij1 = Vij(i, j-1, h);
    let vij2 = Vij(i-1, j-1, h);
    return ( (2*vij.0+vij1.0+vij2.0)/4,(2*vij.1+vij1.1+vij2.1)/4 )
}
fn zijminus1minus1(i: i8, j: i8, h: f32) -> (f32,f32) {
    let vij = Vij(i,j,h);
    let vij1 = Vij(i-1, j-1, h);
    let vij2 = Vij(i-1, j, h);
    return ( (2*vij.0+vij1.0+vij2.0)/4,(2*vij.1+vij1.1+vij2.1)/4 )
}
fn zijminus10(i: i8, j: i8, h: f32) -> (f32,f32) {
    let vij = Vij(i,j,h);
    let vij1 = Vij(i-1, j, h);
    let vij2 = Vij(i, j+1, h);
    return ( (2*vij.0+vij1.0+vij2.0)/4,(2*vij.1+vij1.1+vij2.1)/4 )
}
fn zij01(i: i8, j: i8, h: f32) -> (f32,f32) {
    let vij = Vij(i,j,h);
    let vij1 = Vij(i, j+1, h);
    let vij2 = Vij(i+1, j+1, h);
    return ( (2*vij.0+vij1.0+vij2.0)/4,(2*vij.1+vij1.1+vij2.1)/4 )
}
fn tij(i: i8, j: i8, h: f32) -> (f32,f32) {
    let vij = Vij(i,j,h);
    let vij1 = Vij(i+1, j+1, h);
    let vij2 = Vij(i+1, j, h);
    return ( (vij.0+vij1.0+vij2.0)/3,(vij.1+vij1.1+vij2.1)/3)
}
fn bij(i: i8, j: i8, h: f32) -> (f32,f32) {
    let vij = Vij(i,j,h);
    let vij1 = Vij(i+1, j+1, h);
    let vij2 = Vij(i, j+1, h);
    return ( (vij.0+vij1.0+vij2.0)/3,(vij.1+vij1.1+vij2.1)/3)
}
fn wij11(i: i8, j: i8, h: f32) -> (f32,f32) {
    let vij = Vij(i,j,h);
    let vij1 = Vij(i+1, j+1, h);
    return ( (2*vij.0+vij1.0)/3,(2*vij.1+vij1.1)/3)
}
fn wij10(i: i8, j: i8, h: f32) -> (f32,f32) {
    let vij = Vij(i,j,h);
    let vij1 = Vij(i+1, j, h);
    return ( (2*vij.0+vij1.0)/3,(2*vij.1+vij1.1)/3)
}
fn wij0minus1(i: i8, j: i8, h: f32) -> (f32,f32) {
    let vij = Vij(i,j,h);
    let vij1 = Vij(i, j-1, h);
    return ( (2*vij.0+vij1.0)/3,(2*vij.1+vij1.1)/3)
}
fn wijminus1minus1(i: i8, j: i8, h: f32) -> (f32,f32) {
    let vij = Vij(i,j,h);
    let vij1 = Vij(i-1, j-1, h);
    return ( (2*vij.0+vij1.0)/3,(2*vij.1+vij1.1)/3)
}
fn wijminus10(i: i8, j: i8, h: f32) -> (f32,f32) {
    let vij = Vij(i,j,h);
    let vij1 = Vij(i-1, j, h);
    return ( (2*vij.0+vij1.0)/3,(2*vij.1+vij1.1)/3)
}
fn wij01(i: i8, j: i8, h: f32) -> (f32,f32) {
    let vij = Vij(i,j,h);
    let vij1 = Vij(i, j+1, h);
    return ( (2*vij.0+vij1.0)/3,(2*vij.1+vij1.1)/3)
}