import matplotlib.pyplot as plt

def plot_match_report(match_report):
    labels = list(match_report.keys())
    stats = [float(val.split('/')[0])/float(val.split('/')[1]) for val in match_report.values()]

    fig, ax = plt.subplots(figsize=(6, 4))
    ax.bar(labels, stats)
    ax.set_ylim([0, 1])
    ax.set_ylabel("Match Percentage")
    ax.set_title("Section-wise Match with Job Description")
    return fig
