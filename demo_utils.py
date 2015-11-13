import matplotlib.pyplot as pl

from astroML.plotting.tools import draw_ellipse

def fake_data_plot(x_true, y_true, x, y, samples=None, mus=None, Vs=None):
    """
    Two column plot of fake data in xd-demo.ipynb
    """
    fig = pl.figure(figsize=(5, 3.75))
    fig.subplots_adjust(left=0.1, right=0.95,
                        bottom=0.1, top=0.95,
                        wspace=0.02, hspace=0.02)

    if samples == None:
        ax1 = fig.add_subplot(121)
        ax2 = fig.add_subplot(122)
        ax3 = ax4 = None
        xcheck=(None, None)
    else:
        ax1 = fig.add_subplot(221)
        ax2 = fig.add_subplot(222)

        ax3 = fig.add_subplot(223)
        ax3.scatter(samples[:, 0], samples[:, 1], s=4, lw=0, c='k')

        ax4 = fig.add_subplot(224)
        for i in range(mus.shape[0]):
            draw_ellipse(mus[i], Vs[i], scales=[2], ax=ax4,
                         ec='k', fc='gray', alpha=0.2)

        xcheck=(0, 1)
    ax1.scatter(x_true, y_true, s=4, lw=0, c='k')
    ax2.scatter(x, y, s=4, lw=0, c='k')

    titles = ["True Distribution", "Noisy Distribution",
              "Extreme Deconvolution\n  resampling",
              "Extreme Deconvolution\n  cluster locations"]

    ax = [ax1, ax2, ax3, ax4]

    for i in range(4):
        if ax[i] is not None:
            ax[i].set_xlim(-1, 13)
            ax[i].set_ylim(-6, 16)

            ax[i].xaxis.set_major_locator(pl.MultipleLocator(4))
            ax[i].yaxis.set_major_locator(pl.MultipleLocator(5))

            ax[i].text(0.05, 0.95, titles[i],
                       ha='left', va='top', transform=ax[i].transAxes)

            if i in xcheck:
                ax[i].xaxis.set_major_formatter(pl.NullFormatter())
            else:
                ax[i].set_xlabel('$x$')

            if i in (1, 3):
                ax[i].yaxis.set_major_formatter(pl.NullFormatter())
            else:
                ax[i].set_ylabel('$y$')

    pl.show()
