import csv
import os
import shutil


results = {}
conflicts = {}


with open("./sample-semantic-conflicts.csv") as sample_conflicts:
    conflicts = csv.DictReader(sample_conflicts, skipinitialspace=True, delimiter=",")
    row = next(conflicts)
    while row["BuildManager"] != "Gradle":
        row = next(conflicts)

    print(row["BuildManager"])
    row["ProjectName"] = row["Project"].split("/")[-1]

    if not os.path.isdir(row["ProjectName"]):
        os.system("git clone " + row["Project"])

    shutil.copyfile(
        "./post-merge", "./" + row["ProjectName"] + "/.git/hooks/post-merge"
    )

    os.chdir("./" + row["ProjectName"])
    os.system("git checkout " + row["Commit"])
    head = row["Commit"]
    parents = os.popen("git log --pretty=%P -n 1 HEAD").read().rstrip()
    base = os.popen("git merge-base " + parents).read().rstrip()
    command = (
        "java -jar C:/Users/DAVID/Documents/repositorios/TCC/miningForStudy/git-driver-static-1.0-SNAPSHOT.jar "
        + head
        + " "
        + parents
        + " "
        + base
        + " "
        + "C:/Users/DAVID/Documents/repositorios/TCC/miningForStudy"
    )

    os.system(command)
    # os.system("bash ./.git/hooks/post-merge " + head + " " + parents + " " + base)

# for row in conflicts:
#
#    print(row)
