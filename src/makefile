INSTALLDIR=~/.local/share/mcos-about
install:
	mkdir -p $INSTALLDIR
	cp mcos-about tux-logo.png $INSTALLDIR
	chmod +x $INSTALLDIR/mcos-about
	sudo ln -sf $INSTALLDIR/mcos-about /usr/bin/mcos-about
uninstall:
	sudo rm /usr/bin/mcos-about
	rm -rf $INSTALLDIR
	