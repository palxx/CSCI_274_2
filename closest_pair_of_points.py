import math

# Function to calculate the Euclidean distance between two points
def distance(point1, point2):
    return math.sqrt((point1[0] - point2[0]) ** 2 + (point1[1] - point2[1]) ** 2)

# Brute force method for finding the closest pair within a small set of points
def brute_force(points):
    min_dist = float('inf')
    closest_pair = (None, None)
    n = len(points)
    for i in range(n):
        for j in range(i + 1, n):
            dist = distance(points[i], points[j])
            if dist < min_dist:
                min_dist = dist
                closest_pair = (points[i], points[j])
    return min_dist, closest_pair

# Function to find the closest pair of points in a strip
def strip_closest(strip, d):
    min_dist = d
    closest_pair = (None, None)
    strip.sort(key=lambda point: point[1])  # Sort by y-coordinate
    n = len(strip)
    for i in range(n):
        j = i + 1
        while j < n and (strip[j][1] - strip[i][1]) < min_dist:
            dist = distance(strip[i], strip[j])
            if dist < min_dist:
                min_dist = dist
                closest_pair = (strip[i], strip[j])
            j += 1
    return min_dist, closest_pair

# Recursive function to find the closest pair of points
def closest_pair_recursive(points_sorted_x, points_sorted_y):
    n = len(points_sorted_x)
    
    # Base case for 3 or fewer points
    if n <= 3:
        return brute_force(points_sorted_x)
    
    # Divide points into two halves
    mid = n // 2
    mid_point = points_sorted_x[mid]
    
    left_half_x = points_sorted_x[:mid]
    right_half_x = points_sorted_x[mid:]
    left_half_y = list(filter(lambda x: x[0] <= mid_point[0], points_sorted_y))
    right_half_y = list(filter(lambda x: x[0] > mid_point[0], points_sorted_y))
    
    # Recursively find the closest pairs in each half
    dl, pair_left = closest_pair_recursive(left_half_x, left_half_y)
    dr, pair_right = closest_pair_recursive(right_half_x, right_half_y)
    
    # Find the smaller of the two distances
    d = min(dl, dr)
    closest_pair = pair_left if dl < dr else pair_right
    
    # Check the strip area near the dividing line for closer points
    strip = [p for p in points_sorted_y if abs(p[0] - mid_point[0]) < d]
    d_strip, pair_strip = strip_closest(strip, d)
    
    # Return the smallest distance found and the corresponding pair of points
    if d_strip < d:
        return d_strip, pair_strip
    else:
        return d, closest_pair

# Main function to find the closest pair of points
def closest_pair(points):
    # Sort points by x and y coordinates
    points_sorted_x = sorted(points, key=lambda point: point[0])
    points_sorted_y = sorted(points, key=lambda point: point[1])
    
    # Use the recursive function to find the closest pair
    return closest_pair_recursive(points_sorted_x, points_sorted_y)

# Testing the function with randomly generated points
import random

# Generate 20 random points within the 2D space (0, 0) to (40, 40)
points = [(random.randint(0, 40), random.randint(0, 40)) for _ in range(20)]
print("Generated Points:", points)

# Find the closest pair of points
min_distance, closest_points = closest_pair(points)
print("Minimum Distance:", min_distance)
print("Closest Pair of Points:", closest_points)
