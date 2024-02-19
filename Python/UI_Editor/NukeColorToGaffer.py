import Gaffer
import imath

Gaffer.Metadata.registerValue( parent, "serialiser:milestoneVersion", 1, persistent=False )
Gaffer.Metadata.registerValue( parent, "serialiser:majorVersion", 3, persistent=False )
Gaffer.Metadata.registerValue( parent, "serialiser:minorVersion", 3, persistent=False )
Gaffer.Metadata.registerValue( parent, "serialiser:patchVersion", 0, persistent=False )

__children = {}

__children["Nuke_Color_to_gaffer"] = Gaffer.Box( "Nuke_Color_to_gaffer" )
parent.addChild( __children["Nuke_Color_to_gaffer"] )
__children["Nuke_Color_to_gaffer"].addChild( Gaffer.Node( "Node" ) )
__children["Nuke_Color_to_gaffer"]["Node"]["user"].addChild( Gaffer.Color3fPlug( "Nuke_garde_color", defaultValue = imath.Color3f( 0, 0, 0 ), flags = Gaffer.Plug.Flags.Default | Gaffer.Plug.Flags.Dynamic, ) )
__children["Nuke_Color_to_gaffer"]["Node"]["user"].addChild( Gaffer.Color3fPlug( "Gaffer_light_color", defaultValue = imath.Color3f( 0, 0, 0 ), flags = Gaffer.Plug.Flags.Default | Gaffer.Plug.Flags.Dynamic, ) )
__children["Nuke_Color_to_gaffer"]["Node"]["user"].addChild( Gaffer.Color3fPlug( "ColorCorrect_final", defaultValue = imath.Color3f( 0, 0, 0 ), flags = Gaffer.Plug.Flags.Default | Gaffer.Plug.Flags.Dynamic, ) )
__children["Nuke_Color_to_gaffer"]["Node"]["user"].addChild( Gaffer.StringPlug( "paster_nuke_node", defaultValue = '', flags = Gaffer.Plug.Flags.Default | Gaffer.Plug.Flags.Dynamic, ) )
__children["Nuke_Color_to_gaffer"]["Node"].addChild( Gaffer.V2fPlug( "__uiPosition", defaultValue = imath.V2f( 0, 0 ), flags = Gaffer.Plug.Flags.Default | Gaffer.Plug.Flags.Dynamic, ) )
__children["Nuke_Color_to_gaffer"].addChild( Gaffer.Color3fPlug( "Gaffer_light_color", defaultValue = imath.Color3f( 0, 0, 0 ), flags = Gaffer.Plug.Flags.Default | Gaffer.Plug.Flags.Dynamic, ) )
__children["Nuke_Color_to_gaffer"].addChild( Gaffer.Expression( "Expression" ) )
__children["Nuke_Color_to_gaffer"]["Expression"]["__in"].addChild( Gaffer.Color3fPlug( "p0", defaultValue = imath.Color3f( 0, 0, 0 ), flags = Gaffer.Plug.Flags.Default | Gaffer.Plug.Flags.Dynamic, ) )
__children["Nuke_Color_to_gaffer"]["Expression"]["__in"].addChild( Gaffer.StringPlug( "p1", defaultValue = '', flags = Gaffer.Plug.Flags.Default | Gaffer.Plug.Flags.Dynamic, ) )
__children["Nuke_Color_to_gaffer"]["Expression"]["__out"].addChild( Gaffer.Color3fPlug( "p0", direction = Gaffer.Plug.Direction.Out, defaultValue = imath.Color3f( 0, 0, 0 ), flags = Gaffer.Plug.Flags.Default | Gaffer.Plug.Flags.Dynamic, ) )
__children["Nuke_Color_to_gaffer"]["Expression"]["__out"].addChild( Gaffer.Color3fPlug( "p1", direction = Gaffer.Plug.Direction.Out, defaultValue = imath.Color3f( 0, 0, 0 ), flags = Gaffer.Plug.Flags.Default | Gaffer.Plug.Flags.Dynamic, ) )
__children["Nuke_Color_to_gaffer"]["Expression"].addChild( Gaffer.V2fPlug( "__uiPosition", defaultValue = imath.V2f( 0, 0 ), flags = Gaffer.Plug.Flags.Default | Gaffer.Plug.Flags.Dynamic, ) )
__children["Nuke_Color_to_gaffer"].addChild( Gaffer.Color3fPlug( "Final_color", defaultValue = imath.Color3f( 0, 0, 0 ), flags = Gaffer.Plug.Flags.Default | Gaffer.Plug.Flags.Dynamic, ) )
__children["Nuke_Color_to_gaffer"].addChild( Gaffer.StringPlug( "user_paster_nuke_node", defaultValue = '', flags = Gaffer.Plug.Flags.Default | Gaffer.Plug.Flags.Dynamic, ) )
__children["Nuke_Color_to_gaffer"].addChild( Gaffer.V2fPlug( "__uiPosition", defaultValue = imath.V2f( 0, 0 ), flags = Gaffer.Plug.Flags.Default | Gaffer.Plug.Flags.Dynamic, ) )
Gaffer.Metadata.registerValue( __children["Nuke_Color_to_gaffer"], 'documentation:url', '' )
Gaffer.Metadata.registerValue( __children["Nuke_Color_to_gaffer"], 'icon', 'boxNode.png' )
Gaffer.Metadata.registerValue( __children["Nuke_Color_to_gaffer"], 'noduleLayout:customGadget:addButtonTop:visible', False )
Gaffer.Metadata.registerValue( __children["Nuke_Color_to_gaffer"], 'noduleLayout:customGadget:addButtonBottom:visible', False )
Gaffer.Metadata.registerValue( __children["Nuke_Color_to_gaffer"], 'noduleLayout:customGadget:addButtonLeft:visible', False )
Gaffer.Metadata.registerValue( __children["Nuke_Color_to_gaffer"], 'noduleLayout:customGadget:addButtonRight:visible', False )
Gaffer.Metadata.registerValue( __children["Nuke_Color_to_gaffer"], 'description', 'A container for "subgraphs" - node networks which exist inside the\nBox and can be exposed by promoting selected internal plugs onto the\noutside of the Box.\n\nBoxes can be used as an organisational tool for simplifying large\ngraphs by collapsing them into sections which perform distinct tasks.\nThey are also used for authoring files to be used with the Reference\nnode.' )
__children["Nuke_Color_to_gaffer"]["Node"]["user"]["Nuke_garde_color"].setInput( __children["Nuke_Color_to_gaffer"]["Expression"]["__out"]["p1"] )
Gaffer.Metadata.registerValue( __children["Nuke_Color_to_gaffer"]["Node"]["user"]["Nuke_garde_color"], 'nodule:type', '' )
__children["Nuke_Color_to_gaffer"]["Node"]["user"]["Gaffer_light_color"].setInput( __children["Nuke_Color_to_gaffer"]["Gaffer_light_color"] )
Gaffer.Metadata.registerValue( __children["Nuke_Color_to_gaffer"]["Node"]["user"]["Gaffer_light_color"], 'nodule:type', '' )
__children["Nuke_Color_to_gaffer"]["Node"]["user"]["ColorCorrect_final"].setInput( __children["Nuke_Color_to_gaffer"]["Expression"]["__out"]["p0"] )
Gaffer.Metadata.registerValue( __children["Nuke_Color_to_gaffer"]["Node"]["user"]["ColorCorrect_final"], 'nodule:type', '' )
__children["Nuke_Color_to_gaffer"]["Node"]["user"]["paster_nuke_node"].setInput( __children["Nuke_Color_to_gaffer"]["user_paster_nuke_node"] )
Gaffer.Metadata.registerValue( __children["Nuke_Color_to_gaffer"]["Node"]["user"]["paster_nuke_node"], 'nodule:type', '' )
Gaffer.Metadata.registerValue( __children["Nuke_Color_to_gaffer"]["Node"]["user"]["paster_nuke_node"], 'plugValueWidget:type', 'GafferUI.MultiLineStringPlugValueWidget' )
__children["Nuke_Color_to_gaffer"]["Node"]["__uiPosition"].setValue( imath.V2f( -8.55000019, 6.5 ) )
Gaffer.Metadata.registerValue( __children["Nuke_Color_to_gaffer"]["Gaffer_light_color"], 'nodule:color', imath.Color3f( 0.689999998, 0.537800014, 0.228300005 ) )
Gaffer.Metadata.registerValue( __children["Nuke_Color_to_gaffer"]["Gaffer_light_color"], 'deletable', True )
Gaffer.Metadata.registerValue( __children["Nuke_Color_to_gaffer"]["Gaffer_light_color"], 'renameable', True )
Gaffer.Metadata.registerValue( __children["Nuke_Color_to_gaffer"]["Gaffer_light_color"], 'nodule:type', '' )
Gaffer.Metadata.registerValue( __children["Nuke_Color_to_gaffer"]["Gaffer_light_color"]["r"], 'nodule:color', imath.Color3f( 0.246700004, 0.376199991, 0.469999999 ) )
Gaffer.Metadata.registerValue( __children["Nuke_Color_to_gaffer"]["Gaffer_light_color"]["g"], 'nodule:color', imath.Color3f( 0.246700004, 0.376199991, 0.469999999 ) )
Gaffer.Metadata.registerValue( __children["Nuke_Color_to_gaffer"]["Gaffer_light_color"]["b"], 'nodule:color', imath.Color3f( 0.246700004, 0.376199991, 0.469999999 ) )
__children["Nuke_Color_to_gaffer"]["Expression"]["__in"]["p0"].setInput( __children["Nuke_Color_to_gaffer"]["Node"]["user"]["Gaffer_light_color"] )
__children["Nuke_Color_to_gaffer"]["Expression"]["__in"]["p1"].setInput( __children["Nuke_Color_to_gaffer"]["Node"]["user"]["paster_nuke_node"] )
__children["Nuke_Color_to_gaffer"]["Expression"]["__uiPosition"].setValue( imath.V2f( -19.0495453, 6.49918938 ) )
__children["Nuke_Color_to_gaffer"]["Final_color"].setInput( __children["Nuke_Color_to_gaffer"]["Node"]["user"]["ColorCorrect_final"] )
Gaffer.Metadata.registerValue( __children["Nuke_Color_to_gaffer"]["Final_color"], 'nodule:type', '' )
Gaffer.Metadata.registerValue( __children["Nuke_Color_to_gaffer"]["user_paster_nuke_node"], 'deletable', True )
Gaffer.Metadata.registerValue( __children["Nuke_Color_to_gaffer"]["user_paster_nuke_node"], 'renameable', True )
Gaffer.Metadata.registerValue( __children["Nuke_Color_to_gaffer"]["user_paster_nuke_node"], 'nodule:type', '' )
Gaffer.Metadata.registerValue( __children["Nuke_Color_to_gaffer"]["user_paster_nuke_node"], 'plugValueWidget:type', 'GafferUI.MultiLineStringPlugValueWidget' )
__children["Nuke_Color_to_gaffer"]["__uiPosition"].setValue( imath.V2f( -34.176384, -56.9938316 ) )
__children["Nuke_Color_to_gaffer"]["Expression"]["__engine"].setValue( 'python' )
__children["Nuke_Color_to_gaffer"]["Expression"]["__expression"].setValue( 'import imath\n\n\ndef string_Split(Selfstring,leftreplaceString,rightreplaceString,num1,num2):\n    return Selfstring.split(leftreplaceString)[num1].split(rightreplaceString)[num2].split()\n\ndef ThreeColorValue(ListName):\n    R = eval(ListName[0])\n    G = eval(ListName[1])\n    B = eval(ListName[2])\n    RGB = (R,G,B)\n    return RGB\n\nnuke_Node_string = parent["__in"]["p1"]\nmultiply_String = string_Split(nuke_Node_string,\'{\',\'}\',2,0)\nparent["__out"]["p1"] = imath.Color3f( ThreeColorValue(multiply_String) )\nlight_ColorValue = str(parent["__in"]["p0"]).replace(","," ")\nlight_ColorValue = string_Split(light_ColorValue,\'(\',\')\',1,0)\nnukeColor_value = ThreeColorValue(multiply_String)\ngafferColor_value = ThreeColorValue(light_ColorValue)\nfinalColor_value = ()\nfor i in range(len(nukeColor_value)):\n    finalColor_value += (nukeColor_value[i] * gafferColor_value[i],)\nparent["__out"]["p0"] = imath.Color3f( finalColor_value )' )


del __children
