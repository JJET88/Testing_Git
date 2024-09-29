def TriangleArea(H,W):
    Triangle =0.5 * H * W
    return Triangle

Height =float(input("Enter Height: "))
Width =float(input("Enter Width: "))

# print("Triangle Area =",TriangleArea(Height,Width))
print(f"Triangle Area = {TriangleArea(Height,Width)}")