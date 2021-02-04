INSTALLDIR = ~/.local/share/about-this-mc
install:
	mkdir -p $(INSTALLDIR)
	cp about-this-mc $(INSTALLDIR)
	chmod +x $(INSTALLDIR)/about-this-mc
	sudo ln -sf $(INSTALLDIR)/about-this-mc /usr/bin/about-this-mc
uninstall:
	sudo rm /usr/bin/about-this-mc
	rm -rf $(INSTALLDIR)
	
