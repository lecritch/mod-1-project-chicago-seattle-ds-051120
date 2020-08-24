
# South King County Opportunity Youth

This project offers an updated estimate of the number of Opportunity Youth in South King County using the 2017 5-year American Community Survey [(ACS)](https://www.census.gov/programs-surveys/acs/about.html) Public Use Microdata Survey [(PUMS)](https://www.census.gov/programs-surveys/acs/technical-documentation/pums.html).

## BACKGROUND

Measuring the successes and barriers faced by our most vulnerable youth is a challenge in the South King County region<sup>1</sup>. While there is a lot of information gathered from K12 districts and colleges about student outcomes, few data exists among Opportunity Youth (OY): young folks between the age 16 through 24 who are disengaged from both work and school<sup>2</sup>. This population is of particular interest to The Seattle Region Partnership (SRP), a multi-sector initiative founded by the Seattle Metropolitan Chamber of Commerce, Seattle Foundation, City of Seattle, and King County<sup>3</sup>.

## PROJECT GOAL

The SRP would like an update on the estimated number of OY in South King County. According to a recent The Seattle Times article, the number of OY in South King County has remained steadfast at 19,000<sup>4</sup>. However, that estimation comes from a report that is over three years old. As Data Science Consultants, your task is to inform the SRP on the current status of OY in South King County using updated data.

## THIS REPOSITORY

### Setup Instructions

If you are missing required software (e.g. Anaconda, PostgreSQL), please run the following command in Bash (designed for Mac computers):
```bash
# installs necessary requirements
# note: this may take anywhere from 10-20 minutes
sh src/requirements/install.sh
```

For Windows and Linux computers, you may need to manually ensure that you have installed [Anaconda](https://docs.anaconda.com/anaconda/install/) and [PostgreSQL](https://www.enterprisedb.com/downloads/postgres-postgresql-downloads).

### `oy-env` conda Environment

This project relies on you using the [`environment.yml`](environment.yml) file to recreate the `oy-env` conda environment. To do so, please run the following commands *in your terminal*:

```bash
# create the oy-env conda environment
conda env create -f environment.yml

# activate the oy-env conda environment
conda activate oy-env

# if needed, make oy-env available to you as a kernel in jupyter
python -m ipykernel install --user --name oy-env --display-name "Python 3 (oy-env)"
```

Note that this may take 10 or more minutes depending on internet speed.

**Windows Note:** The same versions of these packages are not available for Windows computers, so all Windows users should use the `windows.yml` file instead of `environment.yml` (this file was generated on Windows 10)

**Linux Note:** The same versions of these packages are not available for Linux computers, so all Linux users should use the `linux.yml` file instead of `environment.yml` (this file was generated on Red Hat)

**Catalina Note:** You may need to modify the `prefix` at the very bottom of `environment.yml` if you are on macOS Catalina.  Run `conda env list` in your terminal to determine the appropriate path by looking at the paths of your existing conda environment(s).  Modify `environment.yml` then try running the installation commands listed above again.

On all operating systems, you will know that you have the required software if the following Bash commands do not return error or "not found" messages:
```bash
which conda
conda list geopandas
which psql
```

### Data Download

To download the relevant data, run the following command *in Python*:

```
data_collection.download_data_and_load_into_sql()
```

Note that this may take 10 or more minutes depending on internet speed.

There is an example notebook in the `notebooks/exploratory` directory with this code already added.


## Citations

<sup>1</sup> Yohalem, N., Cooley, S. 2016. “Opportunity Youth in the Road Map Project Region”. Community Center for Education Results. Available at: https://bit.ly/2P2XRF3.

<sup>2</sup> Anderson, T., Braga, B., Derrick-Mills, T., Dodkowitz, A., Peters, E., Runes, C., and Winkler, M. 2019. “New Insights into the Back on Track Model’s Effects on Opportunity Youth Outcomes”. Urban Institute. Available at: https://bit.ly/2BuCLr1.

<sup>3</sup> Seattle Region Partnership. 2016. “King County Opportunity Youth Overview: Demographics of opportunity youth and systemic barriers to employment”. Available at: https://bit.ly/2oRGz37.

<sup>4</sup> Morton, N. 2019. “Nearly 19,000 youth in King County are neither working nor in school. How one Seattle nonprofit is changing that.” The Seattle Times. Available at: https://bit.ly/2W5EufR.
