bl_info = {
    "name": "Zoom Tool",
    "author": "Zeatrex",
    "version": (1, 0),
    "blender": (4, 00, 0),
    "location": "Sidebar > View > Zoom Tools",
    "description": "Provides tools for zooming to 3D cursor and resetting zoom level.",
    "warning": "",
    "wiki_url": "",
    "category": "3D View"
}

import bpy
from bpy.types import Operator, Panel

# Define Operator for zooming to cursor
class OBJECT_OT_ZoomToCursor(Operator):
    bl_idname = "object.zoom_to_cursor"
    bl_label = "Focus 3D Cursor"
    bl_description = "Focus the view to the 3D cursor"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):
        # Get the 3D cursor location
        cursor_location = bpy.context.scene.cursor.location
        
        # Set the view center to the cursor location
        context.region_data.view_location = cursor_location
        
        return {'FINISHED'}

# Define Operator for resetting zoom
class OBJECT_OT_ResetZoom(Operator):
    bl_idname = "object.reset_zoom"
    bl_label = "Zoom"
    bl_description = "Resets the zoom level to default"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):
        # Reset zoom
        context.space_data.region_3d.view_distance = 5.0  # Default zoom level (adjust as needed)
        
        return {'FINISHED'}

# Define Panel
class VIEW3D_PT_ZoomToolsPanel(Panel):
    bl_label = "Zoom Tool"
    bl_idname = "VIEW3D_PT_zoom_tools"
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_category = 'View'

    def draw(self, context):
        layout = self.layout

        # Zoom to Cursor button
        layout.operator("object.zoom_to_cursor", text="Zoom to 3D Cursor")
        
        # Reset Zoom button
        layout.operator("object.reset_zoom", text="Reset Zoom")

def register():
    bpy.utils.register_class(OBJECT_OT_ZoomToCursor)
    bpy.utils.register_class(OBJECT_OT_ResetZoom)
    bpy.utils.register_class(VIEW3D_PT_ZoomToolsPanel)

def unregister():
    bpy.utils.unregister_class(OBJECT_OT_ZoomToCursor)
    bpy.utils.unregister_class(OBJECT_OT_ResetZoom)
    bpy.utils.unregister_class(VIEW3D_PT_ZoomToolsPanel)

if __name__ == "__main__":
    register()
