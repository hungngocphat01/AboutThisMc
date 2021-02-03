INSTALLDIR = ~/.local/share/mcos-about
install:
	mkdir -p $(INSTALLDIR)
	cp mcos-about* $(INSTALLDIR)
	chmod +x $(INSTALLDIR)/mcos-about*
	sudo ln -sf $(INSTALLDIR)/mcos-about /usr/bin/mcos-about
	sudo ln -sf $(INSTALLDIR)/mcos-about-noterm /usr/bin/mcos-about-noterm
uninstall:
	sudo rm /usr/bin/mcos-about
	sudo rm /usr/bin/mcos-about-noterm
	rm -rf $(INSTALLDIR)
	