# Description
This is a Python package for estimating the location of cells recorded with Neuropixels within the mouse brain

# Installation
Clone the repository:<br />
`git clone https://github.com/felsenlab/unit-localizer.git`<br />
<br />
Navigate to the root directory of the project:<br />
`cd ./unit-localizer`<br />
<br />
Execute the setup script with pip:<br />
`pip install .`

# Basic usage
## Downloading the Allen Mouse Common Coordinate Framework (CCF)
```Python
from unit_localizer import downloadCCFDataFromOSF
downloadCCFDataFromOSF()
```
The function `downloadCCFDataFromOSF` downloads the CCF to your local machine.
Alternatively, you can download the CCF from a different source using the
`downloadCCFDataFromAllenInstitute` function. It should be the same data.<br />

## Estimating unit location with the Neuropixels trajectory explorer
```Python
from unit_localizer import localizeUnitsWithTrajectoryExplorerFile
kilosortOutputFolder = 'path/to/kilosort/output'
trajectoryExplorerFile = 'path/to/trajectory/explorere/file'
labels, points, transformed = localizeUnitsWithTrajectoryExplorerFile(
    kilosortOutputFolder=kilosortOutputFolder
    trajectoryExplorerFile=trajectoryExplorerFile
)
```
`labels` is an array of the brain structures associated with each unit. `points`
is an array (N units x 3) with the coordinates of each unit in voxels of the
Allen Common Coordinate Framework. `transformed` is an array with the same shape
as `points` but indicates the location of each unit in stereotaxic coordinates
in reference to bregma.<br />
## Estimating unit location with sterotaxic coordinates
```Python
from unit_localizer import localizeUnitsWithInsertionParameters
kilosortOutputFolder = 'path/to/kilosort/output'
insertionPoint = np.array([-3.9, 2.5, 0.4]) # Insertion point in sterotaxic coordinates (AP, ML, DV) in mm
insertionDepth = 3.6 # Depth of insertion along the trajectory of the insertion (in mm)
insertionAngle = 6 # Angle of insertion (in degrees)
skullThickness = 0.3 # Assumed thickness of the skull (in mm)
labels, points, transformed = localizeUnitsWithInsertionParameters(
    kilosortOutputFolder=kilosortOutputFolder,
    insertionPoint=insertionPoint,
    insertionDepth=insertionDepth,
    insertionAngle=insertionAngle,
    skullThickness=skullThickness
)
```
## Utility functions
The `estimateSpikeDepths` function computes the distance of each spike from the tip of the Neurpixels
probe. Please note that this function assumes all active channels are clustered
at the tip of the electrode.<br />
```Python
from unit_localizer import estimateSpikeDepths
kilosortOutputFolder = 'path/to/kilosort/output'
templateDepths, spikeDepths = estimateSpikeDepths(
    kilosortOutputFolder=kilosortOutputFolder
)
```