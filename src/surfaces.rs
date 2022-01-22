use crate::curves::Point2D;

pub struct Point3D {
    x: f32,
    y: f32,
    z: f32,
}
trait BezierSurface {
    fn decasteljau_surfaces(points: &[Point2D]) -> Vec<Point2D>;
    fn degree_elevation(points: &[Point2D], degree: i32) -> Vec<Point2D>;
    fn interpolant_surfaces(
        left: f32,
        right: f32,
        step_long: f32,
        function: fn(f32) -> f32,
    ) -> Vec<Point3D>;
    // easy on the surfaces one, there is a lot of things to define first
}
