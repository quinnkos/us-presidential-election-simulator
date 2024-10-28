from tkinter import Tk, Canvas, Label, Scale, Button
import pandas as pd

from variables import *
import simulator


def prepareRun(wn, mainCanvas):
    # gathers data
    data = pd.read_csv(str(yearScale.get()) + "_election_results.csv")
    # ensures dataframe starts with alabama and ends with wyoming; resets index
    firstStateIdx = data[data.iloc[:, 0] == next(x for x in data.iloc[:, 0] if str(x).startswith("Al"))].index.values[0]
    data = data.iloc[:, 0:-1].iloc[firstStateIdx:firstStateIdx + 56]
    data = data.dropna(how='all').reset_index(drop=True)

    # reorganize 2020 dataframe
    if yearScale.get() == 2020:
        data = pd.concat([
            data.iloc[0:20],
            data.iloc[22:24],
            data.iloc[20:22],
            data.iloc[24:29],
            data.iloc[38:39],
            data.iloc[35:38],
            data.iloc[29:35],
            data.iloc[39:]
        ]).reset_index(drop=True)

    # removes irrelevant columns
    i = 0
    while i < len(data.columns):
        if "%" not in data.loc[:, data.columns[i]][1]:
            data.drop(data.columns[i], axis=1, inplace=True)
        else:
            i += 2

    # converts electoral votes to integers
    data.loc[:, data.columns[1]] = list(map(int, [x if x != "–" and x != "-" else 0 for x in data.iloc[:, 1]]))
    data.loc[:, data.columns[3]] = list(map(int, [x if x != "–" and x != "-" else 0 for x in data.iloc[:, 3]]))

    # creates new dataframe with dem vote %, dem+rep vote %, and electoral votes
    demIdx = 0 if yearScale.get() >= 2008 else 2
    newData = pd.DataFrame(data={
        "demPercent": list(data.iloc[:, demIdx].str[:-1].astype(float) - (skewScale.get() / 2)),
        "demRepPercent": list(
            x + y for x, y in zip(map(float, data.iloc[:, 0].str[:-1]), map(float, data.iloc[:, 2].str[:-1]))),
        "EV": data.iloc[:, 1::2].apply(pd.to_numeric, errors='coerce').fillna(0).astype(int).sum(axis=1)
    })

    # Add missing electoral vote to Minnesota
    if yearScale.get() == 2004:
        newData.loc[26, "EV"] += 1

    assert newData.EV.sum() == 538, "%d electoral votes counted in dataset; expected 538" % (newData["EV"].sum())

    # stores nominee display names in variables
    demNominee = str(demNominees[int((yearScale.get() - 2000) / 4)])
    repNominee = str(repNominees[int((yearScale.get() - 2000) / 4)])
    roP = roPScale.get()

    titleLabel.destroy()
    yearLabel.destroy()
    yearScale.destroy()
    roPLabel.destroy()
    roPScale.destroy()
    skewLabel.destroy()
    skewScale.destroy()
    runButton.destroy()

    # runs simulator
    simulator.run(wn, mainCanvas, newData, demNominee, repNominee, roP)


def main():

    global mainCanvas
    global titleLabel
    global yearLabel
    global yearScale
    global roPLabel
    global roPScale
    global skewLabel
    global skewScale
    global runButton

    wn = Tk()
    wn.title('U.S. Presidential Election Simulator')
    wn.geometry('1366x768')
    wn.config(bg=wnColor)

    mainCanvas = Canvas(wn, width=1366, height=768, bg=wnColor, highlightthickness=0)
    mainCanvas.place(x=0, y=0)

    titleLabel = Label(wn, text='U.S. PRESIDENTIAL ELECTION SIMULATOR', font=(mainFont, 45), fg='black', bg=wnColor)
    titleLabel.pack(pady=80)

    yearLabel = Label(wn, text='Year of Election:', font=(mainFont, 18), fg='black', bg=wnColor)
    yearLabel.place(x=613, y=175)
    yearScale = Scale(wn, font=(mainFont, 14), fg='black', bg=wnColor, from_=2000, to=2020, orient='horizontal',
                      length=200, resolution=4)
    yearScale.place(x=583, y=208)
    yearScale.set(2020)

    roPLabel = Label(wn, text='Range of Possibility:', font=(mainFont, 18), fg='black', bg=wnColor)
    roPLabel.place(x=598, y=288)
    roPScale = Scale(wn, font=(mainFont, 14), fg='black', bg=wnColor, from_=1, to=50, orient='horizontal', length=200,
                     resolution=0.5)
    roPScale.place(x=583, y=323)
    roPScale.set(8)

    skewLabel = Label(wn, text='Skew Dem(-)/Rep(+):', font=(mainFont, 18), fg='black', bg=wnColor)
    skewLabel.place(x=593, y=400)
    skewScale = Scale(wn, font=(mainFont, 14), fg='black', bg=wnColor, from_=-10, to=10, orient='horizontal', length=200,
                      resolution=0.25)
    skewScale.place(x=583, y=433)

    runButton = Button(wn, text='Run', font=(mainFont, 20), fg='black', bg=wnColor, width=8, height=2, borderwidth=0,
                       command=lambda: prepareRun(wn, mainCanvas))
    runButton.place(x=631, y=518)

    wn.mainloop()


if __name__ == '__main__':
    main()
