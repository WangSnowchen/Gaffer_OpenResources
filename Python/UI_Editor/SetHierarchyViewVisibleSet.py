###
#The following code snippet describes a node that uses
#GafferSceneUI.ContextAlgo.setVisibleSet() 
#to control the visibility toggle in the hierarchical structure view. 
#This allows for quick restoration of the previous settings each time the file is reopened.
###

import Gaffer
import GafferScene
import IECore
import imath

Gaffer.Metadata.registerValue( parent, "serialiser:milestoneVersion", 1, persistent=False )
Gaffer.Metadata.registerValue( parent, "serialiser:majorVersion", 3, persistent=False )
Gaffer.Metadata.registerValue( parent, "serialiser:minorVersion", 3, persistent=False )
Gaffer.Metadata.registerValue( parent, "serialiser:patchVersion", 0, persistent=False )

__children = {}

__children["SetVisibleSet"] = Gaffer.Box( "SetVisibleSet" )
parent.addChild( __children["SetVisibleSet"] )
__children["SetVisibleSet"].addChild( GafferScene.PathFilter( "SetVisibleSet" ) )
__children["SetVisibleSet"]["SetVisibleSet"]["user"].addChild( Gaffer.BoolPlug( "BoolPlug1", defaultValue = False, flags = Gaffer.Plug.Flags.Default | Gaffer.Plug.Flags.Dynamic, ) )
__children["SetVisibleSet"]["SetVisibleSet"].addChild( Gaffer.V2fPlug( "__uiPosition", defaultValue = imath.V2f( 0, 0 ), flags = Gaffer.Plug.Flags.Default | Gaffer.Plug.Flags.Dynamic, ) )
__children["SetVisibleSet"].addChild( Gaffer.StringVectorDataPlug( "paths", defaultValue = IECore.StringVectorData( [  ] ), flags = Gaffer.Plug.Flags.Default | Gaffer.Plug.Flags.Dynamic, ) )
__children["SetVisibleSet"].addChild( Gaffer.BoolPlug( "Set", defaultValue = False, flags = Gaffer.Plug.Flags.Default | Gaffer.Plug.Flags.Dynamic, ) )
__children["SetVisibleSet"].addChild( Gaffer.V2fPlug( "__uiPosition", defaultValue = imath.V2f( 0, 0 ), flags = Gaffer.Plug.Flags.Default | Gaffer.Plug.Flags.Dynamic, ) )
Gaffer.Metadata.registerValue( __children["SetVisibleSet"], 'nodeGadget:color', imath.Color3f( 0.560000002, 0.302399993, 0.302399993 ) )
Gaffer.Metadata.registerValue( __children["SetVisibleSet"], 'documentation:url', '' )
Gaffer.Metadata.registerValue( __children["SetVisibleSet"], 'description', 'A container for "subgraphs" - node networks which exist inside the\nBox and can be exposed by promoting selected internal plugs onto the\noutside of the Box.\n\nBoxes can be used as an organisational tool for simplifying large\ngraphs by collapsing them into sections which perform distinct tasks.\nThey are also used for authoring files to be used with the Reference\nnode.' )
Gaffer.Metadata.registerValue( __children["SetVisibleSet"], 'noduleLayout:customGadget:addButtonTop:visible', False )
Gaffer.Metadata.registerValue( __children["SetVisibleSet"], 'noduleLayout:customGadget:addButtonBottom:visible', False )
Gaffer.Metadata.registerValue( __children["SetVisibleSet"], 'noduleLayout:customGadget:addButtonLeft:visible', False )
Gaffer.Metadata.registerValue( __children["SetVisibleSet"], 'noduleLayout:customGadget:addButtonRight:visible', False )
Gaffer.Metadata.registerValue( __children["SetVisibleSet"]["SetVisibleSet"], 'description', 'Chooses locations by matching them against a list of\npaths.' )
Gaffer.Metadata.registerValue( __children["SetVisibleSet"]["SetVisibleSet"]["user"]["BoolPlug1"], 'nodule:type', '' )
Gaffer.Metadata.registerValue( __children["SetVisibleSet"]["SetVisibleSet"]["user"]["BoolPlug1"], 'layout:section', '' )
Gaffer.Metadata.registerValue( __children["SetVisibleSet"]["SetVisibleSet"]["user"]["BoolPlug1"], 'plugValueWidget:type', 'GafferUI.ButtonPlugValueWidget' )
Gaffer.Metadata.registerValue( __children["SetVisibleSet"]["SetVisibleSet"]["user"]["BoolPlug1"], 'buttonPlugValueWidget:clicked', "root = plug.node().scriptNode()\nVisSet = root['PathFilter1']['paths'].getValue()\nfor i in test:\n\tv = GafferSceneUI.ContextAlgo.getVisibleSet( root.context() )\n\tv.inclusions.addPath(f'{VisSet}')\n\tGafferSceneUI.ContextAlgo.setVisibleSet( root.context(), v )" )
Gaffer.Metadata.registerValue( __children["SetVisibleSet"]["SetVisibleSet"]["user"]["BoolPlug1"], 'description', '' )
Gaffer.Metadata.registerValue( __children["SetVisibleSet"]["SetVisibleSet"]["user"]["BoolPlug1"], 'layout:accessory', True )
__children["SetVisibleSet"]["SetVisibleSet"]["paths"].setInput( __children["SetVisibleSet"]["paths"] )
__children["SetVisibleSet"]["SetVisibleSet"]["__uiPosition"].setValue( imath.V2f( 31.4168968, 15.7702904 ) )
Gaffer.Metadata.registerValue( __children["SetVisibleSet"]["paths"], 'description', "The list of paths to the locations to be matched by the filter.\nA path is formed by a sequence of names separated by `/`, and\nspecifies the hierarchical position of a location within the scene.\nPaths may use Gaffer's standard wildcard characters to match\nmultiple locations.\n\nThe `*` wildcard matches any sequence of characters within\nan individual name, but never matches across names separated\nby a `/`.\n\n - `/robot/*Arm` matches `/robot/leftArm`, `/robot/rightArm` and\n   `/robot/Arm`. But does not match `/robot/limbs/leftArm` or\n   `/robot/arm`.\n\nThe `...` wildcard matches any sequence of names, and can be\nused to match locations no matter where they are parented in\nthe hierarchy.\n\n - `/.../house` matches `/house`, `/street/house` and `/city/street/house`." )
Gaffer.Metadata.registerValue( __children["SetVisibleSet"]["paths"], 'nodule:type', '' )
Gaffer.Metadata.registerValue( __children["SetVisibleSet"]["paths"], 'ui:scene:acceptsPaths', True )
Gaffer.Metadata.registerValue( __children["SetVisibleSet"]["paths"], 'vectorDataPlugValueWidget:dragPointer', 'objects' )
Gaffer.Metadata.registerValue( __children["SetVisibleSet"]["paths"], 'plugValueWidget:type', 'GafferSceneUI.PathFilterUI._PathsPlugValueWidget' )
Gaffer.Metadata.registerValue( __children["SetVisibleSet"]["Set"], 'nodule:type', '' )
Gaffer.Metadata.registerValue( __children["SetVisibleSet"]["Set"], 'plugValueWidget:type', 'GafferUI.ButtonPlugValueWidget' )
Gaffer.Metadata.registerValue( __children["SetVisibleSet"]["Set"], 'buttonPlugValueWidget:clicked', "import Gaffer\nimport GafferSceneUI\n\nroot = plug.node().scriptNode()\nVisSet = root['SetVisibleSet']['paths'].getValue()\nfor i in VisSet:\n\tv = GafferSceneUI.ContextAlgo.getVisibleSet( root.context() )\n\tv.inclusions.addPath(f'{i}')\n\tGafferSceneUI.ContextAlgo.setVisibleSet( root.context(), v )" )
Gaffer.Metadata.registerValue( __children["SetVisibleSet"]["Set"], 'description', '' )
__children["SetVisibleSet"]["__uiPosition"].setValue( imath.V2f( 16.1663609, -87.4258041 ) )


del __children

