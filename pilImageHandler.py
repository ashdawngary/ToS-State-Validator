'''
ocr image graber, interfaced into tkinter.
use pageflipping to rapidly display images.
'''
import ImageTk
class PageFlipperImageDisplayer:
    def __init__(self,predef,labelInstance):
        '''
        predef is the PIL Image Generic Background image thing.
        '''
        self.cLabelInstance = labelInstance
        self.page1 = ImageTk.PhotoImage(predef)
        self.page2 = ImageTk.PhotoImage(predef)
        self.p1write = False
        self.p2write = False
        self.modewrite = False
        self.newest = None
    def write(self,newim):
        if self.modewrite and not self.p1write:
            # write page 1
            self.modewrite = not self.modewrite
            self.p1write = True
            self.page1 = ImageTk.PhotoImage(newim)
            self.p1write = False
            self.cLabelInstance.config(image=self.page1)
            self.newest = newim
        elif not self.modewrite and not self.p2write:
            self.modewrite = not self.modewrite
            self.p1write = True
            self.page2 = ImageTk.PhotoImage(newim)
            self.p2write = False
            self.cLabelinstance.config(image=self.page1)
            self.newest = newim
    def queryNewestImage(self):
        return self.newest
