from ase.calculators.vasp import Vasp

#default parameters for calculators
defaults = {
	'xc': 'PBE',
	'ivdw': 12,
	'encut': 520,
	'prec': 'Accurate',
	'algo': 'All',
	'ediff': 1e-4,
	'ediffxl': 1e-6,
	'nelm': 150,
	'nelmxl': 150,
	'nelmin': 3,
	'lreal': False,
	'ismear': 0,
	'sigma': 0.01,
	'nsw': 500,
	'ediffg': -0.03,
	'lorbit': 11,
	'isym': 0,
	'symprec': 1e-8,
	'setups': {'base':'recommended','Li':'','W':'_sv','Eu':'_3','Yb':'_3'},
	'ldau_luj': None,
	'lasph': False,
	'nupdown': -1
	}

def calcs(calc_name):
	"""
	Define the default calculators for relaxations
	Note: it should not include the kpts, gamma, or images keywords!
	Args:
		calc_name (string): name of calculator
		
	Returns:
		calc (dict): ASE Vasp calculator dictionary
	"""
	if calc_name == 'scf_test':
		calc = Vasp(
			xc=defaults['xc'],
			setups=defaults['setups'],
			encut=defaults['encut'],
			ivdw=defaults['ivdw'],
			prec=defaults['prec'],
			algo=defaults['algo'],
			ediff=defaults['ediffxl'],
			nelm=defaults['nelmxl'],
			lreal=False,
			ismear=defaults['ismear'],
			sigma=defaults['sigma'],
			lcharg=True,
			laechg=True,
			lwave=True,
			nsw=0,
			lorbit=defaults['lorbit'],
			isym=defaults['isym'],
			symprec=defaults['symprec'],
			addgrid=False,
			ldau_luj=defaults['ldau_luj'],
			lasph=defaults['lasph'],
			nupdown=defaults['nupdown']
			)
	elif calc_name == 'ase_bfgs':
		calc = Vasp(
			xc=defaults['xc'],
			setups=defaults['setups'],
			ivdw=defaults['ivdw'],
			prec=defaults['prec'],
			algo=defaults['algo'],
			ediff=defaults['ediff'],
			nelm=defaults['nelm']*1.5,
			nelmin=defaults['nelmin'],
			lreal=defaults['lreal'],
			ismear=defaults['ismear'],
			sigma=defaults['sigma'],
			lcharg=False,
			lwave=True,
			lorbit=defaults['lorbit'],
			isym=defaults['isym'],
			symprec=defaults['symprec'],
			ldau_luj=defaults['ldau_luj'],
			lasph=defaults['lasph'],
			nupdown=defaults['nupdown']
			)
	elif calc_name == 'isif2_lowacc':
		calc = Vasp(
			xc=defaults['xc'],
			setups=defaults['setups'],
			ivdw=defaults['ivdw'],
			prec=defaults['prec'],
			algo=defaults['algo'],
			ediff=defaults['ediff'],
			nelm=defaults['nelm'],
			nelmin=defaults['nelmin'],
			lreal=defaults['lreal'],
			ismear=defaults['ismear'],
			sigma=defaults['sigma'],
			lcharg=False,
			lwave=True,
			ibrion=2,
			isif=2,
			nsw=250,
			ediffg=-0.05,
			lorbit=defaults['lorbit'],
			isym=defaults['isym'],
			symprec=defaults['symprec'],
			ldau_luj=defaults['ldau_luj'],
			lasph=defaults['lasph'],
			nupdown=defaults['nupdown']
			)
	elif calc_name == 'isif2_medacc':
		calc = Vasp(
			xc=defaults['xc'],
			setups=defaults['setups'],
			ivdw=defaults['ivdw'],
			prec=defaults['prec'],
			algo=defaults['algo'],
			ediff=defaults['ediff'],
			nelm=defaults['nelm'],
			nelmin=8,
			lreal=defaults['lreal'],
			ismear=defaults['ismear'],
			sigma=defaults['sigma'],
			lcharg=False,
			lwave=True,
			ibrion=3,
			iopt=7,
			potim=0,
			isif=2,
			nsw=defaults['nsw'],
			ediffg=-0.05,
			lorbit=defaults['lorbit'],
			isym=defaults['isym'],
			symprec=defaults['symprec'],
			ldau_luj=defaults['ldau_luj'],
			lasph=defaults['lasph'],
			nupdown=defaults['nupdown']
			)
	elif calc_name == 'isif2_highacc':
		calc = Vasp(
			xc=defaults['xc'],
			setups=defaults['setups'],
			encut=defaults['encut'],
			ivdw=defaults['ivdw'],
			prec=defaults['prec'],
			algo=defaults['algo'],
			ediff=1e-6,
			nelm=defaults['nelm'],
			nelmin=8,
			lreal=defaults['lreal'],
			ismear=defaults['ismear'],
			sigma=defaults['sigma'],
			lcharg=False,
			lwave=True,
			ibrion=3,
			iopt=7,
			potim=0,
			isif=2,
			nsw=defaults['nsw'],
			ediffg=defaults['ediffg'],
			lorbit=defaults['lorbit'],
			isym=defaults['isym'],
			symprec=defaults['symprec'],
			ldau_luj=defaults['ldau_luj'],
			lasph=defaults['lasph'],
			nupdown=defaults['nupdown']
			)
	elif calc_name == 'isif3_lowacc':
		calc = Vasp(
			xc=defaults['xc'],
			setups=defaults['setups'],
			encut=defaults['encut'],
			ivdw=defaults['ivdw'],
			prec=defaults['prec'],
			algo=defaults['algo'],
			ediff=defaults['ediffxl'],
			nelm=defaults['nelm'],
			nelmin=defaults['nelmin'],
			lreal=defaults['lreal'],
			ismear=defaults['ismear'],
			sigma=defaults['sigma'],
			lcharg=False,
			lwave=True,
			ibrion=2,
			isif=3,
			nsw=30,
			ediffg=defaults['ediffg'],
			lorbit=defaults['lorbit'],
			isym=defaults['isym'],
			symprec=defaults['symprec'],
			ldau_luj=defaults['ldau_luj'],
			lasph=defaults['lasph'],
			nupdown=defaults['nupdown']
			)
	elif calc_name == 'isif3_highacc':
		calc = Vasp(
			xc=defaults['xc'],
			setups=defaults['setups'],
			encut=defaults['encut'],
			ivdw=defaults['ivdw'],
			prec=defaults['prec'],
			algo=defaults['algo'],
			ediff=defaults['ediffxl'],
			nelm=defaults['nelm'],
			nelmin=defaults['nelmin'],
			lreal=defaults['lreal'],
			ismear=defaults['ismear'],
			sigma=defaults['sigma'],
			lcharg=False,
			lwave=True,
			ibrion=2,
			isif=3,
			nsw=30,
			ediffg=defaults['ediffg'],
			lorbit=defaults['lorbit'],
			isym=defaults['isym'],
			symprec=defaults['symprec'],
			ldau_luj=defaults['ldau_luj'],
			lasph=defaults['lasph'],
			nupdown=defaults['nupdown']
			)
	elif calc_name == 'final_spe':
		calc = Vasp(
			xc=defaults['xc'],
			setups=defaults['setups'],
			encut=defaults['encut'],
			ivdw=defaults['ivdw'],
			prec=defaults['prec'],
			algo=defaults['algo'],
			ediff=defaults['ediffxl'],
			nelm=defaults['nelmxl'],
			lreal=False,
			ismear=defaults['ismear'],
			sigma=defaults['sigma'],
			lcharg=True,
			laechg=True,
			lwave=True,
			nsw=0,
			lorbit=defaults['lorbit'],
			isym=defaults['isym'],
			symprec=defaults['symprec'],
			addgrid=False,
			ldau_luj=defaults['ldau_luj'],
			lasph=defaults['lasph'],
			nupdown=defaults['nupdown']
			)
	elif calc_name == 'cineb_lowacc':
		calc = Vasp(
			xc=defaults['xc'],
			setups=defaults['setups'],
			ivdw=defaults['ivdw'],
			prec=defaults['prec'],
			algo=defaults['algo'],
			ediff=1e-6,
			nelm=100,
			nelmin=defaults['nelmin'],
			lreal=defaults['lreal'],
			ismear=defaults['ismear'],
			sigma=defaults['sigma'],
			lcharg=False,
			lwave=True,
			ibrion=3,
			potim=0,
			iopt=1,
			nsw=defaults['nsw'],
			ediffg=-0.1,
			lclimb=True,
			lorbit=defaults['lorbit'],
			isym=defaults['isym'],
			symprec=defaults['symprec'],
			ichain=0,
			ldau_luj=defaults['ldau_luj'],
			lasph=defaults['lasph'],
			nupdown=defaults['nupdown']
			)
	elif calc_name == 'dimer_lowacc':
		calc = Vasp(
			xc=defaults['xc'],
			setups=defaults['setups'],
			ivdw=defaults['ivdw'],
			prec=defaults['prec'],
			algo=defaults['algo'],
			ediff=1e-8,
			nelm=defaults['nelm'],
			nelmin=defaults['nelmin'],
			lreal=defaults['lreal'],
			ismear=defaults['ismear'],
			sigma=defaults['sigma'],
			lcharg=False,
			lwave=True,
			ibrion=3,
			potim=0,
			iopt=7,
			nsw=defaults['nsw']*4,
			ediffg=-0.075,
			lorbit=defaults['lorbit'],
			isym=defaults['isym'],
			symprec=defaults['symprec'],
			ichain=2,
			ldau_luj=defaults['ldau_luj'],
			lasph=defaults['lasph'],
			nupdown=defaults['nupdown']
			)
	elif calc_name == 'dimer_medacc':
		calc = Vasp(
			xc=defaults['xc'],
			setups=defaults['setups'],
			ivdw=defaults['ivdw'],
			prec=defaults['prec'],
			algo=defaults['algo'],
			ediff=1e-8,
			nelm=defaults['nelm'],
			nelmin=defaults['nelmin'],
			lreal=defaults['lreal'],
			ismear=defaults['ismear'],
			sigma=defaults['sigma'],
			lcharg=False,
			lwave=True,
			ibrion=3,
			potim=0,
			iopt=7,
			nsw=defaults['nsw']*2,
			ediffg=defaults['ediffg'],
			lorbit=defaults['lorbit'],
			isym=defaults['isym'],
			symprec=defaults['symprec'],
			ichain=2,
			ldau_luj=defaults['ldau_luj'],
			lasph=defaults['lasph'],
			nupdown=defaults['nupdown']
			)
	elif calc_name == 'dimer_highacc':
		calc = Vasp(
			xc=defaults['xc'],
			encut=defaults['encut'],
			setups=defaults['setups'],
			ivdw=defaults['ivdw'],
			prec=defaults['prec'],
			algo=defaults['algo'],
			ediff=1e-8,
			nelm=defaults['nelm'],
			nelmin=defaults['nelmin'],
			lreal=defaults['lreal'],
			ismear=defaults['ismear'],
			sigma=defaults['sigma'],
			lcharg=False,
			lwave=True,
			ibrion=3,
			potim=0,
			iopt=7,
			nsw=defaults['nsw']*2,
			ediffg=defaults['ediffg_dimerhigh'],
			lorbit=defaults['lorbit'],
			isym=defaults['isym'],
			symprec=defaults['symprec'],
			ichain=2,
			ldau_luj=defaults['ldau_luj'],
			lasph=defaults['lasph'],
			nupdown=defaults['nupdown']
			)
	else:
		raise ValueError('Out of range for calculators')

	return calc