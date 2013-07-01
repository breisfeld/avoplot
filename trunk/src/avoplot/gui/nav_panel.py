#Copyright (C) Nial Peters 2013
#
#This file is part of AvoPlot.
#
#AvoPlot is free software: you can redistribute it and/or modify
#it under the terms of the GNU General Public License as published by
#the Free Software Foundation, either version 3 of the License, or
#(at your option) any later version.
#
#AvoPlot is distributed in the hope that it will be useful,
#but WITHOUT ANY WARRANTY; without even the implied warranty of
#MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#GNU General Public License for more details.
#
#You should have received a copy of the GNU General Public License
#along with AvoPlot.  If not, see <http://www.gnu.org/licenses/>.
import wx
import warnings
from avoplot import core
from avoplot import figure

class NavigationPanel(wx.ScrolledWindow):
    def __init__(self, parent, session):
        super(NavigationPanel, self).__init__(parent)
        self.SetScrollRate(2, 2)
        self.v_sizer = wx.BoxSizer(wx.VERTICAL)
        self.tree = wx.TreeCtrl(self, wx.ID_ANY, style=wx.TR_HIDE_ROOT|wx.TR_HAS_BUTTONS|wx.TR_LINES_AT_ROOT)
        self.v_sizer.Add(self.tree,1,wx.EXPAND)
        self.__current_selection_id = None
        
        #add the session element as the root node
        root = self.tree.AddRoot(session.get_name(), data=wx.TreeItemData(session))
        self.__el_id_mapping = {session.get_avoplot_id():root}

        core.EVT_AVOPLOT_ELEM_SELECT(self, self.on_element_select)
        core.EVT_AVOPLOT_ELEM_DELETE(self, self.on_element_delete)
        core.EVT_AVOPLOT_ELEM_ADD(self, self.on_element_add)
        core.EVT_AVOPLOT_ELEM_RENAME(self, self.on_element_rename)
        wx.EVT_TREE_SEL_CHANGED(self, self.tree.GetId(), self.on_tree_select_el)
        #do the layout 
        self.SetSizer(self.v_sizer)
        self.v_sizer.Fit(self)
        self.SetAutoLayout(True)
        
    
    def on_tree_select_el(self, evnt):
        #get the avoplot element and set it selected
        tree_node_id = evnt.GetItem()
        el = self.tree.GetPyData(tree_node_id)
        self.__current_selection_id = el.get_avoplot_id()
        el.set_selected()
    
        
    def on_element_select(self, evnt):
        el = evnt.element
        
        #if the element is our current selection, then do nothing
        if el.get_avoplot_id() == self.__current_selection_id:
            return
        
        #if the element exists in the tree then select it
        if self.__el_id_mapping.has_key(el.get_avoplot_id()):
            self.tree.SelectItem(self.__el_id_mapping[el.get_avoplot_id()])
            self.__current_selection_id = el.get_avoplot_id()
            return 
        
        else:
            warnings.warn("element not in tree"+str(el))
        #if the element is new then insert it into the tree
#        else:
#            parent_id = el.get_parent_element().get_avoplot_id()
#            print "added element to tree"
#            self.tree.AppendItem(self.__el_id_mapping[parent_id], el.get_name(),
#                                 data=wx.TreeItemData(el))
        
        #TODO
               
    def on_element_delete(self, evnt):
        print "nav panel on delete",evnt.element.get_name()

        el = evnt.element
        if self.__el_id_mapping.has_key(el.get_avoplot_id()):
            tree_item = self.__el_id_mapping.pop(el.get_avoplot_id())
            self.tree.Delete(tree_item)
    
        
    def on_element_add(self, evnt):
        el = evnt.element
        parent_id = el.get_parent_element().get_avoplot_id()
        if self.__el_id_mapping.has_key(parent_id):
            node = self.tree.AppendItem(self.__el_id_mapping[parent_id], 
                                        el.get_name(), data=wx.TreeItemData(el))
            self.__el_id_mapping[el.get_avoplot_id()] = node
            
            #add all the child elements as well
            for c in el.get_child_elements():
                if not self.__el_id_mapping.has_key(c.get_avoplot_id()):
                    c_node = self.tree.AppendItem(node, 
                                            c.get_name(), data=wx.TreeItemData(c))
                    self.__el_id_mapping[c.get_avoplot_id()] = c_node
    
        
    def on_element_rename(self, evnt):
        el = evnt.element
        if self.__el_id_mapping.has_key(el.get_avoplot_id()):
            tree_node = self.__el_id_mapping[el.get_avoplot_id()]
            self.tree.SetItemText(tree_node, el.get_name())
        
            
        
    def build_new_tree(self, fig):
        self.tree.DeleteAllItems()

        root = self.tree.AddRoot(fig.get_name(), data=wx.TreeItemData(fig))
        self.__el_id_mapping = {fig.get_avoplot_id():root}
        
        for subplot in fig.get_child_elements():
            sbplt_node = self.tree.AppendItem(root, subplot.get_name(), 
                                              data=wx.TreeItemData(subplot))
            self.__el_id_mapping[subplot.get_avoplot_id()] = sbplt_node
            
            for data in subplot.get_child_elements():
                data_node = self.tree.AppendItem(sbplt_node, data.get_name(), 
                                     data=wx.TreeItemData(data))
                self.__el_id_mapping[data.get_avoplot_id()] = data_node
        