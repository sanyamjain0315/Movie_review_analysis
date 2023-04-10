import joblib

# Importing model
model = joblib.load("review_clf")
print("Review sentiment analysis")
while True:
    print("\n")
    # Input review
    ip = [input("Enter your review: ")]
    # 
    op = model.predict(ip)
    print("Review type:",op[0])