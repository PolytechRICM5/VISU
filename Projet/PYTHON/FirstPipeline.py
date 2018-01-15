# state file generated using paraview version 5.4.1

# ----------------------------------------------------------------
# setup views used in the visualization
# ----------------------------------------------------------------

#### import the simple module from the paraview
from paraview.simple import *
#### disable automatic camera reset on 'Show'
paraview.simple._DisableFirstRenderCameraReset()

# Create a new 'Render View'
renderView1 = CreateView('RenderView')
renderView1.UseOffscreenRendering = True
renderView1.UseOffscreenRenderingForScreenshots = True
MonEchelle = 0.5
renderView1.ViewSize = [(int) (2801*MonEchelle),(int) (1791*MonEchelle)]
renderView1.InteractionMode = '2D'
renderView1.OrientationAxesVisibility = 0
renderView1.CenterOfRotation = [2., 46.45, 0.0]
renderView1.CameraPosition = [2., 46.45, 60.]
renderView1.CameraFocalPoint = [2., 46.45, 0.0]
renderView1.CameraParallelScale = 9.
renderView1.CameraParallelProjection = 1
renderView1.Background = [1.0, 1.0, 1.0]
renderView1.UseGradientBackground = 1

# ----------------------------------------------------------------
# setup the data processing pipelines
# ----------------------------------------------------------------

# create a new 'NetCDF Reader'
lecteurNC = NetCDFReader(FileName=[sys.argv[1]])
lecteurNC.Dimensions = '(latitude, longitude)'
lecteurNC.SphericalCoordinates = 0
lecteurNC.OutputType = 'Image'

# create a new 'Extract Subset'
extractSubset1 = ExtractSubset(Input=lecteurNC)
extractSubset1.VOI = [0, 2800, 0, 1790, 0, 0]
extractSubset1.SampleRateI = 50
extractSubset1.SampleRateJ = 50

# create a new 'Calculator'
calculator2 = Calculator(Input=extractSubset1)
calculator2.ResultArrayName = 'temp'
calculator2.Function = 'TMP_2maboveground-273.15'

# create a new 'Threshold'
threshold2 = Threshold(Input=calculator2)
threshold2.Scalars = ['POINTS', 'temp']
threshold2.ThresholdRange = [-20.0, 30.0]

# create a new 'Calculator'
calculator3 = Calculator(Input=threshold2)
calculator3.ResultArrayName = 'Vent'
calculator3.Function = 'UGRD_10maboveground*iHat+VGRD_10maboveground*jHat'

# create a new 'Stream Tracer'
streamTracer1 = StreamTracer(Input=calculator3,
    SeedType='High Resolution Line Source')
streamTracer1.Vectors = ['POINTS', 'Vent']
streamTracer1.MaximumStreamlineLength = 27.0

# init the 'High Resolution Line Source' selected for 'SeedType'
streamTracer1.SeedType.Point1 = [-11.5, 38.0, 0.0]
streamTracer1.SeedType.Point2 = [15.5, 55.0, 0.0]
streamTracer1.SeedType.Resolution = 50

# create a new 'Calculator'
calculator1 = Calculator(Input=lecteurNC)
calculator1.ResultArrayName = 'temp'
calculator1.Function = 'TMP_2maboveground - 273.15'

# create a new 'Threshold'
threshold1 = Threshold(Input=calculator1)
threshold1.Scalars = ['POINTS', 'temp']
threshold1.ThresholdRange = [-50.0, 100.0]

# create a new 'Glyph'
glyph1 = Glyph(Input=calculator3,
    GlyphType='Arrow')
glyph1.Scalars = ['POINTS', 'None']
glyph1.Vectors = ['POINTS', 'Vent']
glyph1.ScaleFactor = 0.6
glyph1.GlyphTransform = 'Transform2'

# ----------------------------------------------------------------
# setup color maps and opacity mapes used in the visualization
# note: the Get..() functions create a new object, if needed
# ----------------------------------------------------------------

# get color transfer function/color map for 'GlyphVector'
glyphVectorLUT = GetColorTransferFunction('GlyphVector')
glyphVectorLUT.RGBPoints = [0.008029546127827617, 0.0, 0.3333333333333333, 0.0, 6.351534366607666, 0.3333333333333333, 0.6666666666666666, 0.0, 18.321453265422193, 1.0, 1.0, 0.0]
glyphVectorLUT.ScalarRangeInitialized = 1.0

# get opacity transfer function/opacity map for 'GlyphVector'
glyphVectorPWF = GetOpacityTransferFunction('GlyphVector')
glyphVectorPWF.Points = [0.008029546127827617, 1.0, 0.5, 0.0, 18.321453265422193, 1.0, 0.5, 0.0]
glyphVectorPWF.ScalarRangeInitialized = 1

# get color transfer function/color map for 'temp'
tempLUT = GetColorTransferFunction('temp')
tempLUT.RGBPoints = [-26.552145385742165, 0.0, 0.0, 0.34902, -25.016653919219948, 0.039216, 0.062745, 0.380392, -23.48116245269773, 0.062745, 0.117647, 0.411765, -21.945670986175514, 0.090196, 0.184314, 0.45098, -20.410179519653298, 0.12549, 0.262745, 0.501961, -18.87468805313108, 0.160784, 0.337255, 0.541176, -17.339196586608864, 0.2, 0.396078, 0.568627, -15.803705120086647, 0.239216, 0.454902, 0.6, -14.26821365356443, 0.286275, 0.521569, 0.65098, -12.732722187042214, 0.337255, 0.592157, 0.701961, -11.197230720519997, 0.388235, 0.654902, 0.74902, -9.66173925399778, 0.466667, 0.737255, 0.819608, -8.126247787475563, 0.572549, 0.819608, 0.878431, -6.590756320953346, 0.654902, 0.866667, 0.909804, -5.05526485443113, 0.752941, 0.917647, 0.941176, -3.519773387908913, 0.823529, 0.956863, 0.968627, -1.984281921386696, 0.941176, 0.984314, 0.988235, -1.984281921386696, 0.988235, 0.960784, 0.901961, -1.0015673828124747, 0.988235, 0.945098, 0.85098, -0.01885284423825695, 0.980392, 0.898039, 0.784314, 1.0867010116577376, 0.968627, 0.835294, 0.698039, 2.6221924781799544, 0.94902, 0.733333, 0.588235, 4.157683944702171, 0.929412, 0.65098, 0.509804, 5.693175411224388, 0.909804, 0.564706, 0.435294, 7.228666877746605, 0.878431, 0.458824, 0.352941, 8.764158344268822, 0.839216, 0.388235, 0.286275, 10.299649810791038, 0.760784, 0.294118, 0.211765, 11.835141277313255, 0.701961, 0.211765, 0.168627, 13.370632743835472, 0.65098, 0.156863, 0.129412, 14.906124210357689, 0.6, 0.094118, 0.094118, 16.441615676879906, 0.54902, 0.066667, 0.098039, 17.977107143402122, 0.501961, 0.05098, 0.12549, 19.51259860992434, 0.45098, 0.054902, 0.172549, 21.048090076446556, 0.4, 0.054902, 0.192157, 22.583581542968773, 0.34902, 0.070588, 0.211765]
tempLUT.ColorSpace = 'Lab'
tempLUT.NanColor = [0.25, 0.0, 0.0]
tempLUT.ScalarRangeInitialized = 1.0

# get opacity transfer function/opacity map for 'temp'
tempPWF = GetOpacityTransferFunction('temp')
tempPWF.Points = [-26.552145385742165, 1.0, 0.5, 0.0, 22.583581542968773, 1.0, 0.5, 0.0]
tempPWF.ScalarRangeInitialized = 1

# ----------------------------------------------------------------
# setup the visualization in view 'renderView1'
# ----------------------------------------------------------------

# show data from threshold1
threshold1Display = Show(threshold1, renderView1)
# trace defaults for the display properties.
threshold1Display.Representation = 'Surface'
threshold1Display.ColorArrayName = ['POINTS', 'temp']
threshold1Display.LookupTable = tempLUT
threshold1Display.OSPRayScaleArray = 'temp'
threshold1Display.OSPRayScaleFunction = 'PiecewiseFunction'
threshold1Display.SelectOrientationVectors = 'None'
threshold1Display.ScaleFactor = 2.8000000000000003
threshold1Display.SelectScaleArray = 'temp'
threshold1Display.GlyphType = 'Arrow'
threshold1Display.GlyphTableIndexArray = 'temp'
threshold1Display.DataAxesGrid = 'GridAxesRepresentation'
threshold1Display.PolarAxes = 'PolarAxesRepresentation'
threshold1Display.ScalarOpacityFunction = tempPWF
threshold1Display.ScalarOpacityUnitDistance = 0.20666834150287358
threshold1Display.GaussianRadius = 1.4000000000000001
threshold1Display.SetScaleArray = ['POINTS', 'temp']
threshold1Display.ScaleTransferFunction = 'PiecewiseFunction'
threshold1Display.OpacityArray = ['POINTS', 'temp']
threshold1Display.OpacityTransferFunction = 'PiecewiseFunction'

# show color legend
threshold1Display.SetScalarBarVisibility(renderView1, True)

# show data from glyph1
glyph1Display = Show(glyph1, renderView1)
# trace defaults for the display properties.
glyph1Display.Representation = 'Surface'
glyph1Display.ColorArrayName = ['POINTS', 'GlyphVector']
glyph1Display.LookupTable = glyphVectorLUT
glyph1Display.OSPRayScaleArray = 'GlyphVector'
glyph1Display.OSPRayScaleFunction = 'PiecewiseFunction'
glyph1Display.SelectOrientationVectors = 'GlyphVector'
glyph1Display.ScaleFactor = 3.0118680000305176
glyph1Display.SelectScaleArray = 'GlyphVector'
glyph1Display.GlyphType = 'Arrow'
glyph1Display.GlyphTableIndexArray = 'GlyphVector'
glyph1Display.DataAxesGrid = 'GridAxesRepresentation'
glyph1Display.PolarAxes = 'PolarAxesRepresentation'
glyph1Display.GaussianRadius = 1.5059340000152588
glyph1Display.SetScaleArray = ['POINTS', 'RH_2maboveground']
glyph1Display.ScaleTransferFunction = 'PiecewiseFunction'
glyph1Display.OpacityArray = ['POINTS', 'RH_2maboveground']
glyph1Display.OpacityTransferFunction = 'PiecewiseFunction'

# show color legend
glyph1Display.SetScalarBarVisibility(renderView1, True)

# show data from streamTracer1
streamTracer1Display = Show(streamTracer1, renderView1)
# trace defaults for the display properties.
streamTracer1Display.Representation = 'Surface'
streamTracer1Display.ColorArrayName = ['POINTS', '']
streamTracer1Display.OSPRayScaleArray = 'temp'
streamTracer1Display.OSPRayScaleFunction = 'PiecewiseFunction'
streamTracer1Display.SelectOrientationVectors = 'Normals'
streamTracer1Display.ScaleFactor = 2.6613832473754884
streamTracer1Display.SelectScaleArray = 'temp'
streamTracer1Display.GlyphType = 'Arrow'
streamTracer1Display.GlyphTableIndexArray = 'temp'
streamTracer1Display.DataAxesGrid = 'GridAxesRepresentation'
streamTracer1Display.PolarAxes = 'PolarAxesRepresentation'
streamTracer1Display.GaussianRadius = 1.3306916236877442
streamTracer1Display.SetScaleArray = ['POINTS', 'temp']
streamTracer1Display.ScaleTransferFunction = 'PiecewiseFunction'
streamTracer1Display.OpacityArray = ['POINTS', 'temp']
streamTracer1Display.OpacityTransferFunction = 'PiecewiseFunction'

# setup the color legend parameters for each legend in this view

# get color legend/bar for tempLUT in view renderView1
tempLUTColorBar = GetScalarBar(tempLUT, renderView1)
tempLUTColorBar.WindowLocation = 'UpperRightCorner'
tempLUTColorBar.Title = 'temp'
tempLUTColorBar.ComponentTitle = ''

# get color legend/bar for glyphVectorLUT in view renderView1
glyphVectorLUTColorBar = GetScalarBar(glyphVectorLUT, renderView1)
glyphVectorLUTColorBar.Title = 'GlyphVector'
glyphVectorLUTColorBar.ComponentTitle = 'Magnitude'

# ----------------------------------------------------------------
# finally, restore active source
SetActiveSource(streamTracer1)
# ----------------------------------------------------------------


# SAUVE UNE COPIE D ECRAN DANS UN FICHIER PNG
WriteImage(sys.argv[1]+".png")
