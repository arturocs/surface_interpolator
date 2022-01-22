pub struct Point2D {
    x: f32,
    y: f32,
}
trait BezierCurve {
    // For the moment is okay on 2D, extension to 3D is easy
    fn bernstein_base_curve(points: &[Point2D]) -> Vec<Point2D>;
    fn decasteljau(points: &[Point2D]) -> Vec<Point2D>;
    fn curve_fix_degree(points: &[Point2D], degree: i32) -> Vec<Point2D>;
    fn curve_from_function(
        left: f32,
        right: f32,
        degree: i32,
        function: fn(f32) -> f32,
    ) -> Vec<Point2D>;
    fn interpolant_cuadratic_class_1(
        left: f32,
        right: f32,
        step_long: f32,
        function: fn(f32) -> f32,
    ) -> Vec<Point2D>;
    fn interpolant_cubic_class_2(
        left: f32,
        right: f32,
        step_long: f32,
        function: fn(f32) -> f32,
    ) -> Vec<Point2D>;
}
