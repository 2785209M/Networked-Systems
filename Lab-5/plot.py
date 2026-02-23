import matplotlib.pyplot as plt

times = []
seqs = []

with open("lab05-timeseq.dat") as f:
    for line in f:
        t, s = line.split()
        seq = int(s)
        if seq > 1_000_000:
            continue  # skip absolute seq number (SYN-ACK)
        hh, mm, ss = t.split(":")
        total_seconds = int(hh) * 3600 + int(mm) * 60 + float(ss)
        times.append(total_seconds)
        seqs.append(seq)

plt.plot(times, seqs, marker=".", markersize=1 ,linewidth="1")
plt.xlabel("Time (s)")
plt.ylabel("Last sequence number")
plt.title("Sequence vs Time")
plt.tight_layout()
plt.savefig("plot.png", dpi=150)