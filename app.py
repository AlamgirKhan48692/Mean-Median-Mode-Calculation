from flask import Flask, render_template, request
from collections import Counter
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

app = Flask(__name__)

# Mean Function
def find_mean(numbers):

    mean = sum(numbers) / len(numbers)

    return mean


# Mode Function
# Mode Function
def find_mode(numbers):

    data = Counter(numbers)

    max_count = max(data.values())

    # No mode case
    if max_count == 1:

        return "No mode found because no number appears more than once."

    modes = []

    for key, value in data.items():

        if value == max_count:

            modes.append(key)

    return modes


# Median Function
def find_median(numbers):

    numbers.sort()

    n = len(numbers)

    middle = n // 2

    # Odd numbers
    if n % 2 != 0:

        median = numbers[middle]

    # Even numbers
    else:

        median = (numbers[middle - 1] + numbers[middle]) / 2

    return median


@app.route("/", methods=["GET", "POST"])
def home():

    mean = None
    mode = None
    median = None

    if request.method == "POST":

        numbers = request.form["numbers"]

        num_list = list(map(int, numbers.split(",")))

        # Function Calls
        mean = find_mean(num_list)

        mode = find_mode(num_list)

        median = find_median(num_list)

        # Handle mode value
        mode_value = mode[0] if isinstance(mode, list) else 0

        labels = ["Mean", "Median", "Mode"]

        values = [mean, median, mode_value]

        plt.figure(figsize=(6,4))

        plt.bar(labels, values)

        plt.title("Statistics Graph")

        plt.ylabel("Values")

        plt.savefig("static/graph.png")

        plt.close()

    return render_template(
        "index.html",
        mean=mean,
        mode=mode,
        median=median
    )

if __name__ == "__main__":
    app.run(debug=True)