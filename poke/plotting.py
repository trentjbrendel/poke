import matplotlib.pyplot as plt
import matplotlib as mpl
import numpy as np

params = {
    'image.origin':'lower',
    'image.interpolation':'nearest',
    'image.cmap':'viridis',
    'axes.labelsize':20,
    'axes.titlesize':24,
    'font.size':20,
    'xtick.labelsize':14,
    'ytick.labelsize':14,
    'figure.figsize':[3.39,2.10],
    'font.family':'serif',
}

mpl.rcParams.update(params)

def AOIPlot(raybundle,surf=-1,units='degrees'):

    xData = raybundle.xData[surf]
    yData = raybundle.yData[surf]
    aoi = raybundle.aoi[surf]

    if units == 'degrees':
        aoi *= 180/np.pi

    plt.figure()
    plt.title('AOI [{uni}] on surface {surface}'.format(uni=units,surface=surf))
    plt.scatter(xData,yData,c=aoi)
    plt.xlabel('[m]')
    plt.ylabel('[m]')
    plt.colorbar()
    plt.show()

def PRTPlot(raybundle,surf=0):

    

    if surf == 0:
        Ptot = raybundle.Ptot
        xData = raybundle.xData[0]
        yData = raybundle.yData[0]
        ampstring = '|PRT Matrix| for System'
        phsstring = 'Arg[PRT Matrix] for System'
    else:
        Ptot = raybundle.P[surf-1]
        xData = raybundle.xData[surf-1]
        yData = raybundle.yData[surf-1]
        ampstring = '|PRT Matrix| for Surface {}'.format(surf)
        phsstring = 'Arg[PRT Matrix] for Surface {}'.format(surf)


    fig,axs = plt.subplots(figsize=[9,9],nrows=3,ncols=3)
    plt.suptitle(ampstring)
    for j in range(3):
        for k in range(3):
            ax = axs[j,k]
            ax.set_title('P{j}{k}'.format(j=j,k=k))
            sca = ax.scatter(xData,yData,c=np.abs(Ptot[j,k,:]))
            ax.axes.xaxis.set_visible(False)
            ax.axes.yaxis.set_visible(False)
            fig.colorbar(sca,ax=ax)
    plt.show()

    fig,axs = plt.subplots(figsize=[9,9],nrows=3,ncols=3)
    plt.suptitle(phsstring)
    for j in range(3):
        for k in range(3):
            ax = axs[j,k]
            ax.set_title('P{j}{k}'.format(j=j,k=k))
            sca = ax.scatter(xData,yData,c=np.angle(Ptot[j,k,:]))
            ax.axes.xaxis.set_visible(False)
            ax.axes.yaxis.set_visible(False)
            fig.colorbar(sca,ax=ax)
    plt.show()

def PlotJonesPupil(raybundle,vmin_amp=None,vmax_amp=None,vmin_opd=None,vmax_opd=None):

    surf = 0

    x = raybundle.xData[surf]
    y = raybundle.yData[surf]
    Jmat = raybundle.Jtot

    fig,axs = plt.subplots(figsize=[9,9],nrows=3,ncols=3)
    plt.suptitle('|Jones Matrix| for System')
    for j in range(3):
        for k in range(3):
            ax = axs[j,k]
            ax.set_title('J{j}{k}'.format(j=j,k=k))
            sca = ax.scatter(x,y,c=np.abs(Jmat[j,k,:]),vmin=vmin_amp,vmax=vmax_amp)
            ax.axes.xaxis.set_visible(False)
            ax.axes.yaxis.set_visible(False)
            fig.colorbar(sca,ax=ax)
    plt.show()

    fig,axs = plt.subplots(figsize=[9,9],nrows=3,ncols=3)
    plt.suptitle('Arg{Jones Matrix} for System')
    for j in range(3):
        for k in range(3):

            # Offset the p coefficient
            if j == 1:
                if k == 1:
                    offset = 0*np.pi
                else:
                    offset = 0
            else:
                offset = 0

            ax = axs[j,k]
            ax.set_title('J{j}{k}'.format(j=j,k=k))
            sca = ax.scatter(x,y,c=np.angle(Jmat[j,k,:])+offset,vmin=vmin_opd,vmax=vmax_opd)
            ax.axes.xaxis.set_visible(False)
            ax.axes.yaxis.set_visible(False)
            fig.colorbar(sca,ax=ax)
    plt.show()
    
def MuellerPupil(M):
    fig,axs = plt.subplots(figsize=[12,12],nrows=4,ncols=4)
    plt.suptitle('Mueller Pupil')
    for i in range(4):
        for j in range(4):
            ax = axs[i,j]
            ax.set_title('J{i}{j}'.format(i=i,j=j))
            sca = ax.imshow(M[i,j,:,:])
            fig.colorbar(sca,ax=ax)
            ax.axes.xaxis.set_visible(False)
            ax.axes.yaxis.set_visible(False)
    plt.show()

def PlotPSM(PSM):
    from matplotlib.colors import LogNorm
    fig,axs = plt.subplots(figsize=[12,12],nrows=4,ncols=4)
    plt.suptitle('Mueller PSM')
    for i in range(4):
        for j in range(4):
            ax = axs[i,j]
            ax.set_title('M{i}{j}'.format(i=i,j=j))
            sca = ax.imshow(PSM[i,j,:,:],norm=LogNorm())
            fig.colorbar(sca,ax=ax)
            ax.axes.xaxis.set_visible(False)
            ax.axes.yaxis.set_visible(False)
    plt.show()

def JonesPlot(raybundle,surf=-1):

    x = raybundle.xData[surf]
    y = raybundle.yData[surf]
    Jmat = raybundle.J[surf]


    fig,axs = plt.subplots(figsize=[9,9],nrows=3,ncols=3)
    plt.suptitle('|Jones Matrix| for Surface in Hubble')
    for j in range(3):
        for k in range(3):
            ax = axs[j,k]
            ax.set_title('J{j}{k}'.format(j=j,k=k))
            sca = ax.scatter(x,y,c=np.abs(Jmat[j,k,:]))
            fig.colorbar(sca,ax=ax)
    plt.show()

    fig,axs = plt.subplots(figsize=[9,9],nrows=3,ncols=3)
    plt.suptitle('Arg{Jones Matrix} for Surface in Hubble')
    for j in range(3):
        for k in range(3):

            # Offset the p coefficient
            if j == 1:
                if k == 1:
                    offset = np.pi
                else:
                    offset = 0
            else:
                offset = 0

            ax = axs[j,k]
            ax.set_title('J{j}{k}'.format(j=j,k=k))
            sca = ax.scatter(x,y,c=np.angle(Jmat[j,k,:])+offset)
            fig.colorbar(sca,ax=ax)
    plt.show()

def PlotRays(raybundle):

    plt.figure(figsize=[12,4])
    plt.subplot(131)
    plt.title('Position')
    plt.scatter(raybundle.xData[0],raybundle.yData[0])

    plt.subplot(132)
    plt.title('Direction Cosine')
    plt.scatter(raybundle.lData[0],raybundle.mData[0])

    plt.subplot(133)
    plt.title('Surface Normal Direction Cosine')
    plt.scatter(raybundle.l2Data[0],raybundle.m2Data[0])
    plt.show()

def PlotJonesArray(J11,J12,J21,J22):

    plt.figure(figsize=[15,7])

    plt.subplot(241)
    plt.imshow(np.abs(J11))
    plt.colorbar()
    plt.title('J00')

    plt.subplot(243)
    plt.imshow(np.angle(J11))
    plt.colorbar()
    plt.title('J00')

    plt.subplot(242)
    plt.imshow(np.abs(J12))
    plt.colorbar()
    plt.title('J01')

    plt.subplot(244)
    plt.imshow(np.angle(J12))
    plt.colorbar()
    plt.title('J00')



    plt.subplot(245)
    plt.imshow(np.abs(J21))
    plt.colorbar()
    plt.title('J10')

    plt.subplot(247)
    plt.imshow(np.angle(J21))
    plt.colorbar()
    plt.title('J10')

    plt.subplot(246)
    plt.imshow(np.abs(J22))
    plt.colorbar()
    plt.title('J11')

    plt.subplot(248)
    plt.imshow(np.angle(J22))
    plt.colorbar()
    plt.title('J11')

    plt.show()



    

