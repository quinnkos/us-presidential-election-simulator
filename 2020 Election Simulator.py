from tkinter import *
import random

wn = Tk()
wn.title('U.S. Presidential Election Simulator')
wn.geometry('1366x768')
wnColor = 'beige'
wn.config(bg=wnColor)

mainFont = 'Palatino'
safeBlue = 'blue'
leanBlue = '#53b9f9'
safeRed = 'red'
leanRed = '#f47e71'
safeBlueState = '#958efe'
leanBlueState = '#c2e6fd'
safeRedState = '#f58a86'
leanRedState = '#f9beb7'
outlineColor = 'black'
uncalledColor = '#cccccc'

demNominee = StringVar()
repNominee = StringVar()

states = ['Alabama', 'Alaska', 'Arizona', 'Arkansas', 'California', 'Colorado', 'Connecticut', 'Delaware', 'District_of_Col', 'Florida', 'Georgia', 'Hawaii', 'Idaho', 'Illinois',
          'Indiana', 'Iowa', 'Kansas', 'Kentucky', 'Louisiana', 'Maine', 'Maine_1', 'Maine_2', 'Maryland', 'Massachusetts', 'Michigan', 'Minnesota', 'Mississippi', 'Missouri', 'Montana',
          'Nebraska', 'Nebraska_1', 'Nebraska_2', 'Nebraska_3', 'Nevada', 'New_Hampshire', 'New_Jersey', 'New_Mexico', 'New_York', 'North_Carolina', 'North_Dakota', 'Ohio', 'Oklahoma',
          'Oregon', 'Pennsylvania', 'Rhode_Island', 'South_Carolina', 'South_Dakota', 'Tennessee', 'Texas', 'Utah', 'Vermont', 'Virginia', 'Washington', 'West_Virginia', 'Wisconsin',
          'Wyoming']

def run(elecVotes, totalDemRep, trueDemVotes):

  roP = roPScale.get()

  for b in range(56):
    trueDemVotes[b] -= skewScale.get()/2

  titleLabel.destroy()
  yearLabel.destroy()
  yearScale.destroy()
  roPLabel.destroy()
  roPScale.destroy()
  skewLabel.destroy()
  skewScale.destroy()
  runButton.destroy()

  demVotes = []

  for y in range(56):
    if y != 19 and y != 29:
      demVotes.append(trueDemVotes[y]+(random.randint(-50*roP, 50*roP))/100)

  demVotes.insert(19, (demVotes[19]*.54086)+(demVotes[20]*.45914))
  demVotes.insert(29, (demVotes[29]*.3556)+(demVotes[30]*.3552)+(demVotes[31]*.2892))

  repVotes = []
  for r in range(56):
    repVotes.append(totalDemRep[r]-demVotes[r])

  for m in range(2):
    headerLabel = Label(wn, text='STATE    ——————    ' + demNominee.get() + '   ' + repNominee.get() + '   VTS', font=(mainFont, 13, 'bold'), bg=wnColor)
    headerLabel.place(x=48+(m*330), y=50)

  dataColors = []
  stateColors = []

  dataXValues = []
  dataYValues = []
  for n in range(56):
    if n <= 27:
      dataXValues.append(43)
      dataYValues.append((n*21)+85)
    else:
      dataXValues.append(373)
      dataYValues.append(dataYValues[n-28])

  for w in range(56):
  
    if demVotes[w] > repVotes[w]:
      if demVotes[w]-5 > repVotes[w]:
        dataColors.append(safeBlue)
        stateColors.append(safeBlueState)
        if demVotes[w] > totalDemRep[w]:
          demVotes[w] = totalDemRep[w]
          repVotes[w] = 0
      else:
        dataColors.append(leanBlue)
        stateColors.append(leanBlueState)
    elif repVotes[w] > demVotes[w]:
      if repVotes[w]-5 > demVotes[w]:
        dataColors.append(safeRed)
        stateColors.append(safeRedState)
        if repVotes[w] > totalDemRep[w]:
          repVotes[w] = totalDemRep[w]
          demVotes[w] = 0
      else:
        dataColors.append(leanRed)
        stateColors.append(leanRedState)
    else:
      if random.randint(0,1) == 0:
        dataColors.append(leanBlue)
        stateColors.append(leanBlueState)
      else:
        dataColors.append(leanRed)
        stateColors.append(leanRedState)
        
    blankStateLabel = Label(wn, text=states[w], fg=uncalledColor, bg=wnColor, font=(mainFont, 14))
    blankStateLabel.place(x=dataXValues[w]+5,y=dataYValues[w])
    blankDemVoteLabel = Label(wn, text='??.??%', fg=uncalledColor, bg=wnColor, font=(mainFont, 14))
    blankDemVoteLabel.place(x=dataXValues[w]+150,y=dataYValues[w])
    blankRepVoteLabel = Label(wn, text='??.??%', fg=uncalledColor, bg=wnColor, font=(mainFont, 14))
    blankRepVoteLabel.place(x=dataXValues[w]+210,y=dataYValues[w])
    blankElecVoteLabel = Label(wn, text=elecVotes[w], fg=uncalledColor, bg=wnColor, font=(mainFont, 14))
    blankElecVoteLabel.place(x=dataXValues[w]+270,y=dataYValues[w])

  dataBorder = mainCanvas.create_rectangle(28, 28, 687, 696)
  dataHalfLine = mainCanvas.create_line(355, 28, 355, 696)

  colorBarX1 = 758
  colorBarY1 = 455
  colorBarX2 = 1296
  colorBarY2 = 465

  demElecVotes = IntVar()
  repElecVotes = IntVar()
  demElecVotes.set(0)
  repElecVotes.set(0)

  colorBar = mainCanvas.create_rectangle(colorBarX1, colorBarY1, colorBarX2, colorBarY2)
  blueBar = mainCanvas.create_rectangle(colorBarX1, colorBarY1, colorBarX1, colorBarY2, fill=safeBlueState)
  redBar = mainCanvas.create_rectangle(colorBarX2, colorBarY1, colorBarX2, colorBarY2, fill=safeRedState)
  twoSeventySplit = mainCanvas.create_line(1027, colorBarY1-7, 1027, colorBarY2+7)

  elecVotesFromCenter = 10
  demElecVotesLabel = Label(wn, textvariable=demElecVotes, fg=safeBlueState, bg=wnColor, font=(mainFont, 42, 'bold'))
  demElecVotesLabel.place(x=1027-elecVotesFromCenter-31, y=520)
  repElecVotesLabel = Label(wn, textvariable=repElecVotes, fg=safeRedState, bg=wnColor, font=(mainFont, 42, 'bold'))
  repElecVotesLabel.place(x=1027+elecVotesFromCenter, y=520)

  logoSize = 130
  extraDistance = 25
  demLogoCanvas = Canvas(wn, width=logoSize, height=logoSize, highlightthickness=0, bg=wnColor)
  demLogoCanvas.place(x=1027-(logoSize*2)+extraDistance, y=520)
  repLogoCanvas = Canvas(wn, width=logoSize, height=logoSize, highlightthickness=0, bg=wnColor)
  repLogoCanvas.place(x=1027+logoSize-extraDistance, y=520)

  shrinkToCircle = 10
  demLogoCircle = demLogoCanvas.create_oval(shrinkToCircle, shrinkToCircle, logoSize-shrinkToCircle, logoSize-shrinkToCircle, width=10, outline='navy blue')
  repLogoCircle = repLogoCanvas.create_oval(shrinkToCircle, shrinkToCircle, logoSize-shrinkToCircle, logoSize-shrinkToCircle, width=10, outline='navy blue')
  demLogoSymbolTop = demLogoCanvas.create_polygon(38, 34, 41, 40, 44, 33, 46, 38, 46, 42, 54, 46, 62, 53, 68, 53, 86, 48, 94, 51, 96, 56, 96, 60, 95, 65, 51, 65, 46, 59, 38, 63, 34, 61,
                                                  38, 45, 36, 41, fill='navy blue', outline=outlineColor)
  demLogoSymbolBottom = demLogoCanvas.create_polygon(51, 68, 95, 68, 95, 70, 100, 75, 100, 79, 95, 72, 94, 73, 95, 83, 94, 86, 94, 94, 91, 98, 86, 98, 85, 97, 88, 94, 88, 90, 89, 88, 89,
                                                     81, 87, 75, 86, 76, 86, 81, 83, 85, 77, 96, 74, 96, 72, 94, 77, 87, 79, 82, 75, 73, 70, 74, 63, 74, 60, 79, 60, 88, 64, 91, 60, 96,
                                                     58, 95, 57, 97, 49, 97, 49, 96, 52, 92, 54, 84, 54, 78, fill='red', outline=outlineColor)
  repLogoSymbolTop = repLogoCanvas.create_polygon(38, 58, 38, 51, 40, 46, 45, 40, 55, 36, 74, 36, 84, 41, 88, 47, 90, 52, 90, 58, fill='navy blue', outline=outlineColor)
  repLogoSymbolBottom = repLogoCanvas.create_polygon(38, 61, 90, 61, 90, 83, 91, 85, 93, 85, 94, 82, 94, 80, 99, 80, 99, 87, 95, 90, 89, 90, 83, 85, 82, 78, 81, 76, 79, 77, 79, 89, 67, 89,
                                                     67, 78, 49, 78, 49, 89, 38, 89, fill='red', outline=outlineColor)

  for d in range(0, 44, 11):
    demLogoStar = demLogoCanvas.create_polygon(52+d, 58, 55+d, 58, 56+d, 55, 57+d, 58, 61+d, 58, 58+d, 61, 59+d, 63, 56+d, 61, 53+d, 63, 54+d, 61, fill=wnColor, outline=outlineColor)
  for r in range(0, 45, 15):
    repLogoStar = repLogoCanvas.create_polygon(46+r, 44, 49+r, 47, 52+r, 44, 51+r, 48, 54+r, 50, 50+r, 50, 49+r, 55, 48+r, 50, 44+r, 50, 47+r, 48, fill=wnColor, outline=outlineColor)

  def newSim():

    global wn
    wn.destroy()
    wn = Tk()
    wn.title('U.S. Presidential Election Simulator')
    wn.geometry('1366x768')
    wn.config(bg=wnColor)
    
    homePage()

  newSimButton = Button(wn, text='New Sim', font=(mainFont, 18), bg=wnColor, width=11, height=2, command=newSim)
  newSimButton.place(x=976, y=620)
  
  mapCanvas = Canvas(wn, width=624, height=390, highlightthickness=0, bg=wnColor)
  mapCanvas.place(x=707, y=12)

  alabama = mapCanvas.create_polygon(426, 250, 454, 248, 461, 275, 465, 284, 464, 290, 466, 302, 437, 305, 439, 310, 438, 315, 435, 316, 432, 309, 430, 315, 427, 315, 424, 294,
                                     fill=uncalledColor, outline=outlineColor)

  alaska = mapCanvas.create_polygon(71, 309, 76, 309, 78, 304, 87, 300, 94, 301, 95, 303, 107, 304, 110, 303, 114, 305, 123, 349, 127, 348, 134, 353, 135, 350, 137, 349, 146, 356, 149, 360,
                                        155, 361, 157, 367, 156, 368, 154, 368, 150, 370, 147, 368, 147, 366, 143, 365, 136, 357, 126, 352, 117, 352, 112, 350, 104, 354, 100, 357, 98, 357,
                                        99, 349, 105, 350, 101, 347, 97, 351, 94, 356, 92, 357, 94, 360, 79, 374, 48, 385, 48, 384, 66, 377, 80, 368, 83, 365, 84, 360, 80, 361, 76, 359, 73, 360,
                                        73, 350, 71, 353, 68, 353, 65, 343, 70, 337, 78, 335, 78, 330, 73, 332, 67, 330, 65, 324, 73, 321, 73, 323, 76, 324, 79, 323, 70, 312, fill=uncalledColor,
                                        outline=outlineColor)
  
  arizona = mapCanvas.create_polygon(140, 208, 194, 216, 184, 295, 161, 291, 120, 267, 123, 264, 124, 264, 125, 261, 123, 260, 123, 255, 127, 252, 127, 248, 132, 244, 130, 240, 129, 233,
                                         131, 218, 134, 218, 138, 220, fill=uncalledColor, outline=outlineColor)

  arkansas = mapCanvas.create_polygon(353, 233, 403, 231, 400, 238, 406, 238, 402, 251, 392, 271, 393, 280, 360, 281, 360, 274, 354, 272, 354, 246, fill=uncalledColor,
                                        outline=outlineColor)

  california = mapCanvas.create_polygon(52, 113, 94, 125, 84, 166, 129, 233, 130, 240, 132, 244, 127, 248, 127, 252, 123, 255, 123, 260, 125, 261, 124, 264, 123, 264, 93, 260, 93, 252,
                                            86, 242, 83, 242, 82, 237, 80, 236, 75, 234, 73, 230, 62, 225, 63, 216, 55, 197, 55, 194, 57, 191, 57, 188, 53, 186, 53, 178, 54, 174, 50, 170,
                                            50, 165, 45, 156, 46, 149, 48, 145, 45, 136, 46, 132, 52, 122, fill=uncalledColor, outline=outlineColor)

  colorado = mapCanvas.create_polygon(202, 161, 275, 167, 272, 224, 194, 216, fill=uncalledColor, outline=outlineColor)

  connecticut = mapCanvas.create_polygon(564, 128, 581, 125, 583, 134, 573, 138, 567, 142, fill=uncalledColor, outline=outlineColor)

  delaware = mapCanvas.create_polygon(548, 165, 550, 163, 552, 163, 551, 167, 554, 170, 554, 173, 559, 177, 560, 181, 552, 182, fill=uncalledColor, outline=outlineColor)

  florida = mapCanvas.create_polygon(437, 305, 466, 302, 468, 306, 500, 304, 502, 306, 503, 300, 508, 300, 514, 314, 525, 329, 523, 330, 535, 349, 535, 363, 533, 373, 524, 375, 524, 373,
                                         520, 366, 517, 365, 501, 346, 503, 340, 498, 344, 499, 327, 488, 320, 484, 315, 477, 313, 477, 316, 465, 320, 465, 318, 452, 311, 438, 315, 439, 310, 
                                         fill=uncalledColor, outline=outlineColor)

  georgia = mapCanvas.create_polygon(454, 248, 480, 244, 479, 249, 485, 251, 489, 256, 503, 268, 510, 280, 512, 280, 508, 300, 503, 300, 502, 306, 500, 304, 468, 306, 466, 302, 464, 290,
                                         465, 284, 461, 275, fill=uncalledColor, outline=outlineColor)

  hawaii = mapCanvas.create_polygon(222, 366, 223, 365, 232, 369, 232, 372, 236, 376, 231, 379, 227, 380, 225, 383, 221, 382, 221, 376, 219, 372, 222, 369, fill=uncalledColor,
                                        outline=outlineColor),
  hawaii2 = mapCanvas.create_polygon(211, 356, 213, 353, 214, 356, 216, 355, 220, 358, 220, 359, 218, 360, 214, 360, 214, 358, fill=uncalledColor, outline=outlineColor)
  hawaii3 = mapCanvas.create_polygon(207, 356, 210, 356, 210, 359, 207, 358, fill=uncalledColor, outline=outlineColor)
  hawaii4 = mapCanvas.create_polygon(204, 352, 211, 352, 209, 354, 203, 354, fill=uncalledColor, outline=outlineColor)
  hawaii5 = mapCanvas.create_polygon(190, 348, 195, 346, 199, 351, 198, 352, 196, 351, 193, 351, fill=uncalledColor, outline=outlineColor)
  hawaii6 = mapCanvas.create_polygon(171, 341, 173, 338, 177, 338, 178, 340, 176, 344, fill=uncalledColor, outline=outlineColor)
  hawaii7 = mapCanvas.create_polygon(165, 343, 167, 341, 168, 343, 165, 344, fill=uncalledColor, outline=outlineColor)

  idaho = mapCanvas.create_polygon(145, 38, 154, 40, 151, 53, 153, 57, 153, 61, 160, 74, 163, 75, 160, 81, 160, 85, 158, 89, 160, 90, 165, 88, 167, 97, 167, 100, 171, 103, 171, 107,
                                       185, 108, 187, 105, 189, 109, 184, 144, 124, 132, 132, 102, 130, 99, 140, 85, 136, 78, fill=uncalledColor, outline=outlineColor)

  illinois = mapCanvas.create_polygon(392, 147, 420, 145, 420, 148, 424, 157, 426, 187, 425, 191, 427, 198, 422, 207, 422, 212, 422, 215, 419, 216, 419, 220, 413, 220, 413, 223, 408, 221,
                                          407, 215, 397, 206, 400, 199, 399, 197, 394, 197, 385, 184, 385, 177, 390, 168, 388, 164, 396, 159, 397, 153, fill=uncalledColor,
                                          outline=outlineColor)

  indiana = mapCanvas.create_polygon(424, 157, 428, 156, 432, 155, 452, 153, 456, 194, 451, 195, 445, 206, 440, 204, 439, 208, 436, 207, 432, 210, 429, 208, 422, 212, 422, 207, 427, 198,
                                          425, 191, 426, 187, fill=uncalledColor, outline=outlineColor)

  iowa = mapCanvas.create_polygon(332, 135, 385, 134, 386, 136, 386, 143, 390, 145, 397, 153, 396, 159, 388, 164, 390, 168, 385, 177, 381, 174, 340, 176, 339, 175, 338, 165, 336, 158,
                                      332, 148, fill=uncalledColor, outline=outlineColor)

  kansas = mapCanvas.create_polygon(274, 183, 342, 184, 348, 186, 346, 190, 352, 196, 353, 226, 272, 224, fill=uncalledColor, outline=outlineColor)

  kentucky = mapCanvas.create_polygon(413, 220, 419, 220, 419, 216, 422, 215, 422, 212, 429, 208, 432, 210, 436, 207, 439, 208, 440, 204, 445, 206, 451, 195, 456, 194, 456, 189, 460, 189,
                                          463, 193, 474, 194, 477, 192, 480, 195, 480, 200, 489, 208, 474, 223, 423, 227, 424, 229, 409, 229, 413, 223, fill=uncalledColor,
                                          outline=outlineColor)

  louisiana = mapCanvas.create_polygon(360, 281, 392, 280, 394, 287, 396, 289, 391, 297, 388, 308, 410, 307, 409, 311, 417, 322, 413, 327, 420, 330, 419, 334, 408, 328, 408, 332, 403, 330,
                                           401, 333, 394, 332, 386, 325, 383, 328, 378, 328, 370, 325, 363, 327, 366, 308, 360, 294, fill=uncalledColor, outline=outlineColor)

  maine = mapCanvas.create_polygon(577, 79, 579, 77, 581, 68, 581, 57, 585, 45, 587, 45, 588, 47, 591, 47, 594, 44, 600, 46, 605, 64, 609, 65, 610, 70, 614, 70, 616, 75, 613, 77, 609, 82,
                                       604, 85, 600, 83, 600, 90, 595, 95, 593, 95, 591, 96, 592, 99, 588, 106, 585, 103, fill=uncalledColor, outline=outlineColor)

  maryland = mapCanvas.create_polygon(510, 172, 548, 165, 552, 182, 560, 181, 557, 188, 553, 189, 551, 185, 547, 185, 548, 180, 545, 174, 547, 167, 545, 172, 543, 173, 544, 180, 547, 187,
                                          537, 186, 539, 179, 529, 174, 525, 170, 522, 170, 521, 173, 518, 173, 511, 180, fill=uncalledColor, outline=outlineColor)

  massachusetts = mapCanvas.create_polygon(564, 118, 583, 115, 587, 109, 590, 114, 589, 118, 593, 120, 595, 125, 600, 123, 601, 125, 594, 128, 593, 126, 589, 130, 586, 123, 581, 125, 
                                               564, 128, fill=uncalledColor, outline=outlineColor)

  michigan = mapCanvas.create_polygon(431, 155, 435, 144, 435, 138, 431, 129, 431, 122, 433, 113, 438, 106, 439, 111, 440, 111, 440, 103, 443, 102, 442, 100, 444, 97, 460, 102, 460, 104,
                                          461, 113, 459, 119, 456, 122, 457, 125, 460, 125, 464, 119, 466, 118, 469, 119, 473, 132, 473, 137, 468, 143, 465, 151, 452, 153, 432, 155,
                                          fill=uncalledColor, outline=outlineColor)
  michigan2 = mapCanvas.create_polygon(391, 90, 397, 87, 400, 87, 410, 77, 412, 79, 409, 82, 408, 85, 410, 84, 416, 84, 419, 89, 426, 90, 429, 86, 441, 84, 441, 87, 448, 87, 450, 86, 
                                           450, 89, 452, 93, 445, 93, 445, 96, 438, 93, 435, 96, 431, 96, 429, 98, 426, 98, 424, 100, 422, 100, 419, 109, 416, 104, 416, 100, 413, 100, 412, 97,
                                           405, 97, 393, 94, fill=uncalledColor, outline=outlineColor)

  minnesota = mapCanvas.create_polygon(326, 60, 344, 60, 344, 55, 347, 55, 349, 61, 359, 64, 364, 63, 370, 68, 372, 66, 379, 70, 382, 69, 397, 71, 385, 77, 372, 91, 372, 99, 366, 105,
                                           369, 108, 369, 118, 384, 128, 385, 134, 332, 135, 332, 109, 328, 106, 332, 103, fill=uncalledColor, outline=outlineColor)

  mississippi = mapCanvas.create_polygon(402, 252, 426, 250, 424, 294, 427, 315, 422, 315, 413, 317, 409, 311, 410, 307, 388, 308, 391, 297, 396, 289, 394, 287, 392, 271,
                                             fill=uncalledColor, outline=outlineColor)

  missouri = mapCanvas.create_polygon(340, 176, 381, 174, 385, 177, 385, 184, 394, 197, 399, 197, 400, 199, 397, 206, 407, 215, 408, 221, 413, 223, 412, 228, 409, 229, 406, 238, 400, 238,
                                          403, 231, 353, 233, 352, 196, 346, 190, 348, 186, 342, 182, fill=uncalledColor, outline=outlineColor)

  montana = mapCanvas.create_polygon(154, 40, 263, 57, 258, 111, 191, 103, 189, 109, 187, 105, 185, 108, 171, 107, 171, 103, 167, 100, 167, 97, 165, 88, 160, 90, 158, 89, 160, 85, 160, 81,
                                         163, 75, 160, 74, 153, 61, 153, 57, 151, 53, fill=uncalledColor, outline=outlineColor)

  nebraska = mapCanvas.create_polygon(256, 138, 312, 141, 316, 144, 323, 143, 332, 148, 334, 150, 338, 165, 339, 175, 344, 184, 274, 183, 275, 168, 254, 166, fill=uncalledColor,
                                            outline=outlineColor)

  nevada = mapCanvas.create_polygon(94, 125, 154, 138, 138, 220, 134, 218, 131, 218, 129, 233, 84, 166, fill=uncalledColor, outline=outlineColor)

  newHampshire = mapCanvas.create_polygon(573, 84, 574, 80, 577, 79, 585, 103, 588, 106, 588, 110, 583, 115, 572, 117, 570, 103, 571, 101, 571, 95, 574, 91, fill=uncalledColor,
                                              outline=outlineColor)

  newJersey = mapCanvas.create_polygon(555, 140, 564, 143, 564, 146, 562, 150, 566, 152, 565, 162, 560, 174, 559, 171, 554, 170, 551, 167, 552, 163, 558, 157, 552, 151, 552, 146,
                                           fill=uncalledColor, outline=outlineColor)

  newMexico = mapCanvas.create_polygon(194, 216, 260, 223, 255, 294, 214, 289, 215, 293, 194, 290, 193, 296, 184, 295, fill=uncalledColor, outline=outlineColor)

  newYork = mapCanvas.create_polygon(501, 138, 508, 129, 507, 125, 505, 124, 505, 122, 514, 120, 526, 119, 533, 113, 532, 105, 538, 94, 541, 91, 556, 88, 559, 97, 559, 100, 560, 106,
                                         562, 108, 564, 118, 564, 128, 567, 142, 568, 143, 580, 140, 580, 142, 574, 145, 568, 148, 564, 148, 564, 146, 564, 143, 555, 140, 551, 139, 550, 136,
                                         546, 133, 502, 142, fill=uncalledColor, outline=outlineColor)

  northCarolina = mapCanvas.create_polygon(494, 220, 556, 209, 559, 215, 556, 213, 548, 219, 555, 217, 557, 221, 560, 217, 560, 222, 557, 226, 555, 227, 552, 226, 554, 229, 552, 232,
                                               557, 232, 557, 234, 552, 236, 548, 237, 540, 251, 535, 251, 520, 240, 507, 242, 506, 240, 502, 239, 488, 240, 480, 244, 467, 246, 473, 238,
                                               490, 227, 494, 222, fill=uncalledColor, outline=outlineColor)

  northDakota = mapCanvas.create_polygon(263, 57, 326, 60, 332, 101, 259, 98, fill=uncalledColor, outline=outlineColor)

  ohio = mapCanvas.create_polygon(452, 153, 465, 151, 476, 154, 483, 152, 494, 143, 498, 163, 495, 178, 488, 183, 487, 187, 484, 188, 484, 194, 480, 195, 477, 192, 474, 194, 463, 193,
                                      460, 189, 456, 189, fill=uncalledColor, outline=outlineColor)
    
  oklahoma = mapCanvas.create_polygon(260, 223, 353, 226, 354, 246, 355, 272, 346, 268, 333, 270, 326, 268, 324, 270, 318, 268, 316, 269, 313, 266, 301, 264, 300, 261, 297, 261,
                                          292, 258, 291, 232, 260, 230, fill=uncalledColor, outline=outlineColor)

  oregon = mapCanvas.create_polygon(73, 58, 82, 63, 83, 70, 88, 72, 92, 71, 98, 74, 118, 74, 137, 78, 141, 85, 130, 99, 132, 102, 124, 132, 94, 125, 52, 113, 53, 102, 62, 88,
                                        fill=uncalledColor, outline=outlineColor)

  pennsylvania = mapCanvas.create_polygon(494, 143, 501, 138, 502, 142, 546, 133, 550, 136, 551, 139, 555, 140, 552, 146, 552, 151, 558, 157, 552, 163, 550, 163, 548, 165, 499, 174,
                                              fill=uncalledColor, outline=outlineColor)

  rhodeIsland = mapCanvas.create_polygon(581, 124, 586, 123, 587, 128, 586, 129, 587, 133, 583, 134, fill=uncalledColor, outline=outlineColor)

  southCarolina = mapCanvas.create_polygon(480, 244, 488, 240, 502, 239, 506, 240, 507, 242, 520, 240, 535, 251, 530, 261, 529, 264, 512, 280, 510, 280, 503, 268, 489, 256, 485, 251,
                                               479, 249, fill=uncalledColor, outline=outlineColor)

  southDakota = mapCanvas.create_polygon(259, 98, 332, 101, 332, 103, 328, 106, 332, 109, 332, 148, 323, 143, 316, 144, 312, 141, 256, 138, fill=uncalledColor, outline=outlineColor)

  tennessee = mapCanvas.create_polygon(409, 229, 424, 229, 423, 227, 494, 220, 494, 222, 490, 227, 473, 238, 467, 246, 402, 252, fill=uncalledColor, outline=outlineColor)

  texas = mapCanvas.create_polygon(259, 230, 293, 232, 292, 258, 297, 261, 300, 261, 301, 264, 313, 266, 316, 269, 318, 268, 324, 270, 326, 268, 333, 270, 346, 268, 355, 272, 360, 275,
                                       360, 294, 366, 308, 363, 327, 352, 331, 352, 327, 349, 328, 350, 332, 347, 337, 338, 343, 331, 343, 318, 361, 323, 378, 321, 380, 298, 373, 293, 357,
                                       285, 346, 281, 335, 272, 325, 262, 323, 256, 326, 253, 333, 249, 334, 235, 325, 232, 312, 215, 294, 214, 289, 255, 293, fill=uncalledColor,
                                       outline=outlineColor)

  utah = mapCanvas.create_polygon(154, 138, 185, 143, 182, 158, 202, 161, 194, 216, 140, 208, fill=uncalledColor, outline=outlineColor)

  vermont = mapCanvas.create_polygon(556, 88, 573, 84, 574, 91, 571, 95, 571, 101, 570, 103, 572, 117, 564, 118, 562, 108, 560, 106, 559, 100, 559, 97, fill=uncalledColor,
                                       outline=outlineColor)

  virginia = mapCanvas.create_polygon(489, 208, 493, 211, 496, 210, 500, 210, 500, 208, 507, 205, 507, 201, 512, 188, 516, 189, 517, 184, 521, 181, 523, 174, 528, 177, 529, 174, 539, 179,  
                                          537, 186, 549, 191, 548, 196, 551, 197, 550, 200, 551, 204, 555, 204, 557, 209, 494, 220, 474, 223, fill=uncalledColor, outline=outlineColor)
  virginia2 = mapCanvas.create_polygon(555, 189, 558, 188, 557, 193, 555, 202, 554, 195, fill=uncalledColor, outline=outlineColor)

  washington = mapCanvas.create_polygon(74, 32, 75, 28, 91, 38, 90, 47, 86, 47, 86, 50, 92, 47, 95, 25, 145, 38, 137, 78, 118, 74, 98, 74, 92, 71, 88, 72, 83, 70, 82, 63, 73, 58, 75, 50,
                                            fill=uncalledColor, outline=outlineColor)

  westVirginia = mapCanvas.create_polygon(497, 162, 499, 174, 510, 173, 511, 180, 518, 173, 521, 173, 522, 170, 525, 170, 529, 174, 528, 177, 523, 174, 521, 181, 517, 184, 516, 189,
                                              512, 188, 507, 201, 507, 205, 500, 208, 500, 210, 496, 210, 493, 211, 489, 208, 480, 200, 480, 195, 484, 194, 484, 188, 487, 187, 488, 183,
                                              495, 178, 498, 163, fill=uncalledColor, outline=outlineColor)

  wisconsin = mapCanvas.create_polygon(372, 91, 374, 89, 376, 91, 386, 86, 386, 90, 391, 90, 393, 94, 405, 97, 412, 97, 413, 100, 416, 100, 416, 104, 419, 109, 415, 115, 416, 116, 424, 107,
                                           425, 108, 422, 113, 418, 137, 420, 141, 420, 145, 392, 147, 390, 145, 386, 143, 386, 136, 385, 134, 385, 134, 384, 128, 369, 118, 369, 108, 366, 105,
                                           372, 99, fill=uncalledColor, outline=outlineColor)

  wyoming = mapCanvas.create_polygon(191, 103, 258, 111, 254, 166, 182, 158, fill=uncalledColor, outline=outlineColor)

  statesCalled = IntVar()
  statesCalled.set(0)
  
  def stateCalled(stateIndex):
    
    def elecVoteUpdate():
      if stateColors[stateIndex+t] == safeBlueState or stateColors[stateIndex+t] == leanBlueState:
        demElecVotes.set(demElecVotes.get()+elecVotes[stateIndex+t])
        mainCanvas.coords(blueBar, colorBarX1, colorBarY1, colorBarX1+demElecVotes.get(), colorBarY2)
        if demElecVotes.get() >= 10 and demElecVotes.get() < 100:
          demElecVotesLabel.place(x=1027-elecVotesFromCenter-52)
        elif demElecVotes.get() >= 100:
          demElecVotesLabel.place(x=1027-elecVotesFromCenter-73)
      else:
        repElecVotes.set(repElecVotes.get()+elecVotes[stateIndex+t])
        mainCanvas.coords(redBar, colorBarX2, colorBarY1, colorBarX2-repElecVotes.get(), colorBarY2)

    if stateIndex == 19:
      for t in range(3):
        elecVoteUpdate()
    elif stateIndex == 29:
      for t in range(4):
        elecVoteUpdate()
    else:
      for t in range(1):
        elecVoteUpdate()
          
    statesCalled.set(statesCalled.get()+1)

    if statesCalled.get() == 51:
      
      layerCanvas = Canvas(wn, width=300, height=600, bg=wnColor, highlightthickness=0)
      layerCanvas.place(x=40, y=80)
      layerCanvas2 = Canvas(wn, width=300, height=600, bg=wnColor, highlightthickness=0)
      layerCanvas2.place(x=360, y=80)
      
      for w in range(56):
        stateLabel = Label(wn, text=states[w], fg=dataColors[w], bg=wnColor, font=(mainFont, 14))
        stateLabel.place(x=dataXValues[w]+5,y=dataYValues[w])
        dem1f = format(demVotes[w], '.1f')
        rep1f = format(repVotes[w], '.1f')
        demVoteLabel = Label(wn, text=str(dem1f.zfill(4)) + '%', fg=dataColors[w], bg=wnColor, font=(mainFont, 14))
        demVoteLabel.place(x=dataXValues[w]+150,y=dataYValues[w])
        repVoteLabel = Label(wn, text=str(rep1f.zfill(4)) + '%', fg=dataColors[w], bg=wnColor, font=(mainFont, 14))
        repVoteLabel.place(x=dataXValues[w]+210,y=dataYValues[w])
        elecVoteLabel = Label(wn, text=elecVotes[w], fg=dataColors[w], bg=wnColor, font=(mainFont, 14))
        elecVoteLabel.place(x=dataXValues[w]+270,y=dataYValues[w])

  def callAlabama():
    mapCanvas.itemconfig(alabama, fill=stateColors[0])
    stateCalled(0)

  def callAlaska():
    mapCanvas.itemconfig(alaska, fill=stateColors[1])
    stateCalled(1)

  def callArizona():
    mapCanvas.itemconfig(arizona, fill=stateColors[2])
    stateCalled(2)

  def callArkansas():
    mapCanvas.itemconfig(arkansas, fill=stateColors[3])
    stateCalled(3)

  def callCalifornia():
    mapCanvas.itemconfig(california, fill=stateColors[4])
    stateCalled(4)
    
  def callColorado():
    mapCanvas.itemconfig(colorado, fill=stateColors[5])
    stateCalled(5)

  def callConnecticut():
    mapCanvas.itemconfig(connecticut, fill=stateColors[6])
    stateCalled(6)

  def callDelaware():
    mapCanvas.itemconfig(delaware, fill=stateColors[7])
    stateCalled(7)

  def callDC():
    stateCalled(8)

  def callFlorida():
    mapCanvas.itemconfig(florida, fill=stateColors[9])
    stateCalled(9)

  def callGeorgia():
    mapCanvas.itemconfig(georgia, fill=stateColors[10])
    stateCalled(10)

  def callHawaii():
    mapCanvas.itemconfig(hawaii, fill=stateColors[11])
    mapCanvas.itemconfig(hawaii2, fill=stateColors[11])
    mapCanvas.itemconfig(hawaii3, fill=stateColors[11])
    mapCanvas.itemconfig(hawaii4, fill=stateColors[11])
    mapCanvas.itemconfig(hawaii5, fill=stateColors[11])
    mapCanvas.itemconfig(hawaii6, fill=stateColors[11])
    mapCanvas.itemconfig(hawaii7, fill=stateColors[11])
    stateCalled(11)

  def callIdaho():
    mapCanvas.itemconfig(idaho, fill=stateColors[12])
    stateCalled(12)

  def callIllinois():
    mapCanvas.itemconfig(illinois, fill=stateColors[13])
    stateCalled(13)

  def callIndiana():
    mapCanvas.itemconfig(indiana, fill=stateColors[14])
    stateCalled(14)

  def callIowa():
    mapCanvas.itemconfig(iowa, fill=stateColors[15])
    stateCalled(15)

  def callKansas():
    mapCanvas.itemconfig(kansas, fill=stateColors[16])
    stateCalled(16)

  def callKentucky():
    mapCanvas.itemconfig(kentucky, fill=stateColors[17])
    stateCalled(17)
    
  def callLouisiana():
    mapCanvas.itemconfig(louisiana, fill=stateColors[18])
    stateCalled(18)

  def callMaine():
    mapCanvas.itemconfig(maine, fill=stateColors[19])
    stateCalled(19)

  def callMaryland():
    mapCanvas.itemconfig(maryland, fill=stateColors[22])
    stateCalled(22)

  def callMassachusetts():
    mapCanvas.itemconfig(massachusetts, fill=stateColors[23])
    stateCalled(23)

  def callMichigan():
    mapCanvas.itemconfig(michigan, fill=stateColors[24])
    mapCanvas.itemconfig(michigan2, fill=stateColors[24])
    stateCalled(24)

  def callMinnesota():
    mapCanvas.itemconfig(minnesota, fill=stateColors[25])
    stateCalled(25)

  def callMississippi():
    mapCanvas.itemconfig(mississippi, fill=stateColors[26])
    stateCalled(26)

  def callMissouri():
    mapCanvas.itemconfig(missouri, fill=stateColors[27])
    stateCalled(27)

  def callMontana():
    mapCanvas.itemconfig(montana, fill=stateColors[28])
    stateCalled(28)

  def callNebraska():
    mapCanvas.itemconfig(nebraska, fill=stateColors[29])
    stateCalled(29)

  def callNevada():
    mapCanvas.itemconfig(nevada, fill=stateColors[33])
    stateCalled(33)

  def callNewHampshire():
    mapCanvas.itemconfig(newHampshire, fill=stateColors[34])
    stateCalled(34)

  def callNewJersey():
    mapCanvas.itemconfig(newJersey, fill=stateColors[35])
    stateCalled(35)

  def callNewMexico():
    mapCanvas.itemconfig(newMexico, fill=stateColors[36])
    stateCalled(36)

  def callNewYork():
    mapCanvas.itemconfig(newYork, fill=stateColors[37])
    stateCalled(37)

  def callNorthCarolina():
    mapCanvas.itemconfig(northCarolina, fill=stateColors[38])
    stateCalled(38)

  def callNorthDakota():
    mapCanvas.itemconfig(northDakota, fill=stateColors[39])
    stateCalled(39)

  def callOhio():
    mapCanvas.itemconfig(ohio, fill=stateColors[40])
    stateCalled(40)

  def callOklahoma():
    mapCanvas.itemconfig(oklahoma, fill=stateColors[41])
    stateCalled(41)

  def callOregon():
    mapCanvas.itemconfig(oregon, fill=stateColors[42])
    stateCalled(42)

  def callPennsylvania():
    mapCanvas.itemconfig(pennsylvania, fill=stateColors[43])
    stateCalled(43)

  def callRhodeIsland():
    mapCanvas.itemconfig(rhodeIsland, fill=stateColors[44])
    stateCalled(44)

  def callSouthCarolina():
    mapCanvas.itemconfig(southCarolina, fill=stateColors[45])
    stateCalled(45)

  def callSouthDakota():
    mapCanvas.itemconfig(southDakota, fill=stateColors[46])
    stateCalled(46)

  def callTennessee():
    mapCanvas.itemconfig(tennessee, fill=stateColors[47])
    stateCalled(47)
    
  def callTexas():
    mapCanvas.itemconfig(texas, fill=stateColors[48])
    stateCalled(48)
    
  def callUtah():
    mapCanvas.itemconfig(utah, fill=stateColors[49])
    stateCalled(49)

  def callVermont():
    mapCanvas.itemconfig(vermont, fill=stateColors[50])
    stateCalled(50)

  def callVirginia():
    mapCanvas.itemconfig(virginia, fill=stateColors[51])
    mapCanvas.itemconfig(virginia2, fill=stateColors[51])
    stateCalled(51)

  def callWashington():
    mapCanvas.itemconfig(washington, fill=stateColors[52])
    stateCalled(52)

  def callWestVirginia():
    mapCanvas.itemconfig(westVirginia, fill=stateColors[53])
    stateCalled(53)

  def callWisconsin():
    mapCanvas.itemconfig(wisconsin, fill=stateColors[54])
    stateCalled(54)

  def callWyoming():
    mapCanvas.itemconfig(wyoming, fill=stateColors[55])
    stateCalled(55)

  timeZoneDifference = 4000
  etCallTime = 0
  ctCallTime = etCallTime+timeZoneDifference
  mtCallTime = ctCallTime+timeZoneDifference
  ptCallTime = mtCallTime+timeZoneDifference
  aktCallTime = ptCallTime+timeZoneDifference
  htCallTime = aktCallTime+timeZoneDifference
  baseCallDelay = 20000
  delayMultiplier = 500
  minimumDelay = 4000

  callDelay = []
  callTime = [ctCallTime, aktCallTime, mtCallTime, ctCallTime, ptCallTime, mtCallTime, etCallTime, etCallTime, etCallTime, etCallTime, etCallTime, htCallTime, mtCallTime, ctCallTime,
              etCallTime, ctCallTime, ctCallTime, etCallTime, ctCallTime, etCallTime, etCallTime, etCallTime, etCallTime, etCallTime, etCallTime, ctCallTime, ctCallTime, ctCallTime,
              mtCallTime, ctCallTime, ctCallTime, ctCallTime, ctCallTime, ptCallTime, etCallTime, etCallTime, mtCallTime, etCallTime, etCallTime, ctCallTime, etCallTime, ctCallTime,
              ptCallTime, etCallTime, etCallTime, etCallTime, ctCallTime, ctCallTime, ctCallTime, mtCallTime, etCallTime, etCallTime, ptCallTime, etCallTime, ctCallTime, mtCallTime]

  leanStateDelay = []
  for m in range(56):
    leanStateDelay.append(10000-callTime[m])

  for n in range(56):
    
    if stateColors[n] == safeBlueState or stateColors[n] == leanBlueState:
      if baseCallDelay-delayMultiplier*(int(demVotes[n])-int(repVotes[n])) >= minimumDelay:
        if stateColors[n] == safeBlueState:
          callDelay.append(baseCallDelay-delayMultiplier*(int(demVotes[n])-int(repVotes[n])))
        else:
          callDelay.append(baseCallDelay+leanStateDelay[n]-delayMultiplier*(int(demVotes[n])-int(repVotes[n])))
      else:
        callDelay.append(minimumDelay)
    else:
      if baseCallDelay-delayMultiplier*(int(repVotes[n])-int(demVotes[n])) >= minimumDelay:
        if stateColors[n] == safeRedState:
          callDelay.append(baseCallDelay-delayMultiplier*(int(repVotes[n])-int(demVotes[n])))
        else:
          callDelay.append(baseCallDelay+leanStateDelay[n]-delayMultiplier*(int(repVotes[n])-int(demVotes[n])))
      else:
        callDelay.append(minimumDelay)
                 
  wn.after(callTime[0]+callDelay[0], callAlabama)
  wn.after((callTime[1]-timeZoneDifference)+callDelay[1], callAlaska)
  wn.after(callTime[2]+callDelay[2], callArizona)
  wn.after(callTime[3]+callDelay[3], callArkansas)
  wn.after(callTime[4]+callDelay[4], callCalifornia)
  wn.after(callTime[5]+callDelay[5], callColorado)
  wn.after(callTime[6]+callDelay[6], callConnecticut)
  wn.after(callTime[7]+callDelay[7], callDelaware)
  wn.after((callTime[8]+timeZoneDifference)+callDelay[8], callDC)
  wn.after(callTime[9]+callDelay[9], callFlorida)
  wn.after(callTime[10]+callDelay[10], callGeorgia)
  wn.after((callTime[11]-timeZoneDifference)+callDelay[11], callHawaii)
  wn.after(callTime[12]+callDelay[12], callIdaho)
  wn.after(callTime[13]+callDelay[13], callIllinois)
  wn.after(callTime[14]+callDelay[14], callIndiana)
  wn.after(callTime[15]+callDelay[15], callIowa)
  wn.after(callTime[16]+callDelay[16], callKansas)
  wn.after(callTime[17]+callDelay[17], callKentucky)
  wn.after(callTime[18]+callDelay[18], callLouisiana)
  wn.after(callTime[19]+callDelay[19], callMaine)
  wn.after(callTime[22]+callDelay[22], callMaryland)
  wn.after(callTime[23]+callDelay[23], callMassachusetts)
  wn.after(callTime[24]+callDelay[24], callMichigan)
  wn.after(callTime[25]+callDelay[25], callMinnesota)
  wn.after(callTime[26]+callDelay[26], callMississippi)
  wn.after(callTime[27]+callDelay[27], callMissouri)
  wn.after(callTime[28]+callDelay[28], callMontana)
  wn.after(callTime[29]+callDelay[29], callNebraska)
  wn.after(callTime[33]+callDelay[33], callNevada)
  wn.after(callTime[34]+callDelay[34], callNewHampshire)
  wn.after(callTime[35]+callDelay[35], callNewJersey)
  wn.after(callTime[36]+callDelay[36], callNewMexico)
  wn.after(callTime[37]+callDelay[37], callNewYork)
  wn.after(callTime[38]+callDelay[38], callNorthCarolina)
  wn.after(callTime[39]+callDelay[39], callNorthDakota)
  wn.after(callTime[40]+callDelay[40], callOhio)
  wn.after(callTime[41]+callDelay[41], callOklahoma)
  wn.after(callTime[42]+callDelay[42], callOregon)
  wn.after(callTime[43]+callDelay[43], callPennsylvania)
  wn.after(callTime[44]+callDelay[44], callRhodeIsland)
  wn.after(callTime[45]+callDelay[45], callSouthCarolina)
  wn.after(callTime[46]+callDelay[46], callSouthDakota)
  wn.after(callTime[47]+callDelay[47], callTennessee)
  wn.after(callTime[48]+callDelay[48], callTexas)
  wn.after(callTime[49]+callDelay[49], callUtah)
  wn.after(callTime[50]+callDelay[50], callVermont)
  wn.after(callTime[51]+callDelay[51], callVirginia)
  wn.after(callTime[52]+callDelay[52], callWashington)
  wn.after(callTime[53]+callDelay[53], callWestVirginia)
  wn.after(callTime[54]+callDelay[54], callWisconsin)
  wn.after(callTime[55]+callDelay[55], callWyoming)

currentElecVotes = [9, 3, 11, 6, 55, 9, 7, 3, 3, 29, 16, 4, 4, 20, 11, 6, 6, 8, 8, 2, 1, 1, 10, 11, 16, 10, 6, 10,
                    3, 2, 1, 1, 1, 6, 4, 14, 5, 29, 15, 3, 18, 7, 7, 20, 4, 9, 3, 11, 38, 6, 3, 13, 12, 5, 10, 3]
previousElecVotes = [9, 3, 10, 6, 55, 9, 7, 3, 3, 27, 15, 4, 4, 21, 11, 7, 6, 8, 9, 2, 1, 1, 10, 12, 17, 10, 6, 11,
                     3, 2, 1, 1, 1, 5, 4, 15, 5, 31, 15, 3, 20, 7, 7, 21, 4, 8, 3, 11, 34, 5, 3, 13, 11, 5, 10, 3]
previousElecVotes2 = [9, 3, 8, 6, 54, 8, 8, 3, 3, 25, 13, 4, 4, 22, 12, 7, 6, 8, 9, 2, 1, 1, 10, 12, 18, 10, 7, 11,
                      3, 2, 1, 1, 1, 4, 4, 15, 5, 33, 14, 3, 21, 8, 7, 23, 4, 8, 3, 11, 32, 5, 3, 13, 11, 5, 11, 3]

def prepareRun():
  
  if yearScale.get() == 2020:
    demNominee.set('BIDEN')
    repNominee.set('TRUMP')
    run(currentElecVotes,
        [98.6, 95.6, 98.42, 97.18, 97.8, 97.3, 98.45, 98.51, 97.55, 99.08, 98.71, 98, 96.91, 98.09, 97.98, 97.98, 97.77, 98.24, 98.31,
         97.11, 97.13, 97.08, 97.51, 97.74, 98.46, 97.68, 98.66, 98.21, 97.47, 97.39, 97.1, 97.4, 97.7, 97.73, 98.07, 98.73, 97.79,
         98.61, 98.52, 96.87, 98.51, 97.66, 96.82, 98.85, 98, 98.54, 97.38, 98.11, 98.54, 95.78, 96.76, 98.11, 96.74, 98.31, 98.27, 96.49],
        [36.57, 42.77, 49.36, 34.78, 63.48, 55.4, 59.26, 58.74, 92.15, 47.86, 49.47, 63.73, 33.07, 57.54, 40.96, 44.89, 41.56, 36.15, 39.85,
         53.09, 60.11, 44.82, 65.36, 65.6, 50.62, 52.4, 41.06, 41.41, 40.55, 39.17, 41.09, 51.95, 22.34, 50.06, 52.71, 57.33, 54.29, 60.86,
         48.59, 31.76, 45.24, 32.29, 56.45, 50.01, 59.39, 43.43, 35.61, 37.45, 46.48, 37.65, 66.09, 54.11, 57.97, 29.69, 49.45, 26.55])
        
  elif yearScale.get() == 2016:
    demNominee.set('CLNTN')
    repNominee.set('TRUMP')
    run(currentElecVotes,
        [96.44, 87.83, 92.66, 94.22, 93.35, 91.41, 95.5, 94.81, 94.55, 96.84, 96.41, 92.25, 86.75, 94.59, 94.73, 92.89, 92.7, 95.2, 96.54,
         92.7, 93.11, 92.24, 94.24, 92.82, 94.77, 91.36, 98.05, 94.91, 91.92, 92.45, 91.64, 92.08, 93.65, 93.42, 93.59, 96.8, 88.3, 95.53,
         96, 90.19, 95.25, 94.25, 89.16, 95.64, 93.31, 95.61, 93.27, 95.44, 95.47, 73, 86.95, 94.14, 89.37, 94.93, 93.67, 90.05],
        [34.36, 36.55, 44.58, 33.65, 61.73, 48.16, 54.57, 53.09, 90.48, 47.82, 45.64, 62.22, 27.49, 55.83, 37.91, 41.74, 36.05, 32.68, 38.45,
         47.83, 53.96, 40.98, 60.33, 60.01, 47.27, 46.44, 40.11, 38.14, 35.75, 33.7, 35.46, 44.92, 19.73, 47.92, 46.98, 55.45, 48.26, 59.01,
         46.17, 27.23, 43.56, 28.93, 50.07, 47.46, 54.41, 40.67, 31.74, 34.72, 43.24, 27.46, 56.68, 49.73, 52.54, 26.43, 46.45, 21.88])

  elif yearScale.get() == 2012:
    demNominee.set('OBAMA')
    repNominee.set('RMNEY')
    run(currentElecVotes,
        [98.91, 95.61, 98.24, 97.45, 97.36, 97.62, 98.79, 98.59, 98.19, 99.14, 98.78, 98.39, 97.15, 98.33, 98.06, 98.17, 97.7, 98.29, 98.36,
         97.25, 97.75, 97.32, 97.87, 98.16, 98.92, 97.61, 99.08, 98.14, 97.05, 97.83, 98.26, 98.55, 98.06, 98.04, 98.38, 98.97, 95.83, 98.52,
         98.74, 97.01, 98.36, 100, 96.39, 98.56, 97.94, 98.65, 97.76, 98.56, 98.55, 97.54, 97.54, 98.44, 97.45, 97.84, 98.72, 96.46],
        [38.36, 40.81, 44.59, 36.88, 60.24, 51.49, 58.06, 58.61, 90.91, 50.01, 45.48, 70.55, 32.62, 57.6, 43.93, 51.99, 37.99, 37.8, 40.58,
         56.27, 59.57, 52.94, 61.97, 60.65, 54.21, 52.65, 43.79, 44.38, 41.7, 38.03, 40.83, 45.7, 27.82, 52.36, 51.98, 58.38, 52.99, 63.35,
         48.35, 38.69, 50.67, 33.23, 52.24, 51.97, 62.7, 44.09, 39.87, 39.08, 41.38, 24.75, 66.57, 51.16, 56.16, 35.54, 52.83, 27.82])

  elif yearScale.get() == 2008:
    demNominee.set('OBAMA')
    repNominee.set('MCAIN')
    run(previousElecVotes,
        [99.06, 97.31, 98.76, 97.58, 97.96, 98.37, 98.81, 98.89, 98.99, 99.25, 99.19, 98.43, 97.61, 98.7, 98.86, 98.32, 98.26, 98.57, 98.49,
         98.09, 98.2, 97.96, 98.39, 97.79, 98.39, 97.88, 99.18, 98.72, 96.76, 98.13, 98.43, 98.72, 98.27, 97.8, 98.65, 98.97, 98.69, 98.91,
         99.08, 97.87, 98.41, 100, 97.15, 98.66, 97.92, 98.77, 97.91, 98.73, 99.13, 96.99, 97.91, 98.96, 98.13, 98.3, 98.53, 97.32],
        [38.74, 37.89, 45.12, 38.86, 61.01, 53.66, 60.59, 61.94, 92.46, 51.03, 46.99, 71.85, 36.09, 61.92, 49.95, 53.93, 41.65, 41.17, 39.93,
         57.71, 60.51, 54.61, 61.92, 61.8, 57.43, 54.06, 43, 49.29, 47.25, 41.6, 44.33, 49.97, 29.63, 55.15, 54.13, 57.27, 56.91, 62.88,
         49.7, 44.62, 51.5, 34.35, 56.75, 54.49, 62.86, 44.9, 44.75, 41.83, 43.68, 34.41, 67.46, 52.63, 57.65, 42.59, 56.22, 32.54])

  elif yearScale.get() == 2004:
    demNominee.set('KERRY')
    repNominee.set('  BUSH ')
    run(previousElecVotes,
        [99.3, 96.59, 99.27, 98.86, 98.67, 98.71, 98.26, 99.1, 98.52, 99.19, 99.34, 99.27, 98.64, 99.3, 99.2, 99.13, 98.62, 99.24, 98.94,
         98.15, 98.21, 98.08, 98.84, 98.72, 99.04, 98.7, 99.21, 99.4, 97.63, 98.58, 98.67, 98.76, 98.65, 98.35, 99.11, 99.16, 98.89,
         98.45, 99.6, 98.36, 99.52, 100, 98.54, 99.34, 98.09, 98.88, 98.35, 99.33, 99.31, 97.54, 97.74, 99.16, 98.46, 99.26, 99.02, 97.93],
        [36.84, 35.52, 44.4, 44.55, 54.31, 47.02, 54.31, 53.35, 89.18, 47.09, 41.37, 54.01, 30.26, 54.82, 39.26, 49.23, 36.62, 39.69, 42.22,
         53.57, 55.07, 51.95, 55.91, 61.94, 51.23, 51.09, 39.76, 46.1, 38.56, 32.68, 35.7, 38.52, 23.73, 47.88, 50.24, 52.92, 49.05, 58.37,
         43.58, 35.5, 48.71, 34.43, 51.35, 50.92, 59.42, 40.9, 38.44, 42.53, 38.22, 26, 58.94, 45.48, 52.82, 43.2, 49.7, 29.07])

  else:
    demNominee.set('  GORE ')
    repNominee.set('  BUSH ')
    run(previousElecVotes2,
        [98.05, 86.29, 95.75, 97.17, 95.1, 93.14, 94.35, 96.86, 94.11, 97.69, 97.65, 93.25, 94.81, 97.18, 97.66, 96.76, 95.28, 97.87, 97.43,
         93.06, 93.11, 92.99, 96.75, 92.3, 97.43, 93.41, 98.32, 97.5, 91.8, 95.5, 94.82, 95.44, 96.29, 95.5, 94.87, 96.42, 95.76, 95.44,
         99.23, 93.72, 96.43, 98.74, 93.48, 97.03, 92.9, 97.74, 97.86, 98.43, 97.28, 93.17, 91.33, 96.91, 94.74, 97.51, 95.44, 95.46],
        [41.57, 27.67, 44.73, 45.86, 53.45, 42.39, 55.91, 54.96, 85.16, 48.84, 42.98, 55.79, 27.64, 54.6, 41.01, 48.54, 37.24, 41.37,
         44.88, 49.09, 50.52, 47.43, 56.57, 59.8, 51.28, 47.91, 40.7, 47.08, 33.36, 33.25, 35.92, 38.52, 24.94, 45.98, 46.8, 56.13, 47.91,
         60.21, 43.2, 33.06, 46.46, 38.43, 46.96, 50.6, 60.99, 40.9, 37.56, 47.28, 37.98, 26.34, 50.63, 44.44, 50.16, 45.59, 47.83, 27.7])

def homePage():

  global mainCanvas
  global titleLabel
  global yearLabel
  global yearScale
  global roPLabel
  global roPScale
  global skewLabel
  global skewScale
  global runButton

  mainCanvas = Canvas(wn, width=1366, height=768, bg=wnColor, highlightthickness=0)
  mainCanvas.place(x=0, y=0)
  
  titleLabel = Label(wn, text='U.S. PRESIDENTIAL ELECTION SIMULATOR', font=(mainFont, 45), fg='black', bg=wnColor)
  titleLabel.pack(pady=80)
  
  yearLabel = Label(wn, text='Year of Election:', font=(mainFont, 18), bg=wnColor)
  yearLabel.place(x=613, y=175)
  yearScale = Scale(wn, font=(mainFont, 14), bg=wnColor, from_=2000, to=2020, orient=HORIZONTAL, length=200, resolution=4)
  yearScale.place(x=583, y=208)
  yearScale.set(2020)
  
  roPLabel = Label(wn, text='Range of Possibility:', font=(mainFont, 18), bg=wnColor)
  roPLabel.place(x=598, y=288)
  roPScale = Scale(wn, font=(mainFont, 14), bg=wnColor, from_=1, to=50, orient=HORIZONTAL, length=200, resolution=0.5)
  roPScale.place(x=583, y=323)
  roPScale.set(8)
  
  skewLabel = Label(wn, text='Skew Dem(-)/Rep(+):', font=(mainFont, 18), bg=wnColor)
  skewLabel.place(x=593, y=400)
  skewScale = Scale(wn, font=(mainFont, 14), bg=wnColor, from_=-10, to=10, orient=HORIZONTAL, length=200, resolution=0.25)
  skewScale.place(x=583, y=433)
  
  runButton = Button(wn, text='Run', font=(mainFont, 20), bg=wnColor, width=10, height=2, command=prepareRun)
  runButton.place(x=631, y=518)

homePage()

wn.mainloop()
