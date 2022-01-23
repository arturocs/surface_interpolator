use rusymbols::{core, Expression};
use bio::stats::combinatorics;
struct F2DPoint {
    x: f32,
    y: f32
}
trait BezierCurve {
    // For the moment is okay on 2D, extension to 3D is easy
    fn bernstein_base_curve(points: &[F2DPoint]) -> Expression;
    fn j_base_element_degree_n(j: i32, n: i32) -> Expression;
    fn decasteljau_method(points: &[F2DPoint]) -> &[F2DPoint];
    fn curve_fix_degree(points: &[F2DPoint], degree: i32) -> &[F2DPoint];
    fn curve_from_function(left: f32, right: f32, degree: i32, function: String) -> &[F2DPoint];
    fn interpolant_cuadratic_class_1(left: f32, right: f32, step_long: f32, function: String) -> &[F2DPoint];
    fn interpolant_cubic_class_2(left: f32, right: f32, step_long: f32, function: String) -> &[F2DPoint];
}

impl BezierCurve for F2DPoint {
    fn decasteljau_method(points: &[F2DPoint]) -> Expression {
        let degree = points.length;
        let exp_iteration = Vec::new();
        for j in 1..degree {
            let mut curve_degree_j = Vec::new();
            for i in 1..(n-j+1) {
                let x = Expression::new_var("x");
                let first_point = Expression::new_val(points[i-1]);
                let second_point = Expression::new_val(points[i]);
                let one = Expression::new_val(-1.0);
                let one_minus_x = Expression::new(one, x, core::Actions::Sub);
                let first_monome = Expression::new(first_point, one_minus_x, core::Actions::Mul);
                let second_monome = Expression::new(second_point, x, core::Actions::Mul);
                let decasteljau_polynom = Expression::new(first_monome, second_monome, core::Actions::Mul);
                curve_degree_j.push(decasteljau_polynom);
            }
            exp_iteration = curve_degree_j.clone();
            curve_degree_j.clear();
        }
        return exp_iteration[0];
    }
    fn j_base_element_degree_n(j: i32, n: i32) -> Expression{
        let j_exp = Expression::new_val(j);
        let n_exp = Expression::new_val(n);
        let t = Expression::new_var("t");
        let one = Expression::new_val(1);
        let one_minus_t = Expression::new(one, t, core::Actions::Sub);
        let combinations = combinatorics::combinations(n,j);
        let n_minus_j = Expression::new(n_exp, j_exp, core::Actions::Sub);
        let first_part = Expression::new(combinations, t.pow(j_exp), core::Actions::Mul);
        let base_polynom = Expression::new(first_part, one_minus_t.pow(n_minus_j), core::Actions::Mul);
        return base_polynom;
    }
    

}

