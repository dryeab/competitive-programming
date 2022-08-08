# Line Geometry

  For point x to be inside of intersection range between two points (a, b) & (c, d), it has to be inside of `a <= x && c <= x && x <= b && x <= d`. Therefore, the intersection would have a length of `max(0, min(b, d) - max(a, c))`.

It can be handled case by case too, when they intersect and they don't (being a < c).

# Rectangular Geometry

Extension of Line Geometry

``` Cpp
struct Rect {

        int x1, x2, y1, y2;

        // (x1, y1) : bottom left
        // (x2, y2) : top right

        int area() {
            int width = x2 - x1, height = y2 - y1;
            return width * height;
        }

        int intersection(Rect other) {
            int xOverlap = max(0, min(x2, other.x2) - max(x1, other.x1));
            int yOverlap = max(0, min(y2, other.y2) - max(y1, other.y1));
            return x * y;
        }
    };

```
