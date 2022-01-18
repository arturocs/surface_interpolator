struct 3DPoint {
    x: f32,
    y: f32,
    z: f32
}
trait BezierSurface {
    fn decasteljau_surfaces(points: &[2DPoint]) -> &[2DPoint]
    fn degree_elevation(points: &[2DPoint], degree: i32) -> &[2DPoint]
    fn interpolant_surfaces(left: f32, right: f32, step_long: f32, function: String) -> &[3DPoint]
    // easy on the surfaces one, there is a lot of things to define first
}
