struct 2DPoint {
    x: f32,
    y: f32
}
trait BezierCurve {
    // For the moment is okay on 2D, extension to 3D is easy
    fn bernstein_base_curve(points: &[2DPoint]) -> &[2DPoint]
    fn decasteljau(points: &[2DPoint]) -> &[2DPoint]
    fn curve_fix_degree(points: &[2DPoint], degree: i32) -> &[2DPoint]
    fn curve_from_function(left: f32, right: f32, degree: i32, function: String) -> &[2DPoint]
    fn interpolant_cuadratic_class_1(left: f32, right: f32, step_long: f32, function: String) -> &[2DPoint]
    fn interpolant_cubic_class_2(left: f32, right: f32, step_long: f32, function: String) -> &[2DPoint]
}
