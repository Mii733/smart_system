$(() => {
    function logEvent(eventName) {
      const logList = $('#events ul');
      const newItem = $('<li>', { text: eventName });
  
      logList.prepend(newItem);
    }
  
    $('#gridContainer').dxDataGrid({
      dataSource: employees,
      keyExpr: 'ID',
      showBorders: true,
      paging: {
        enabled: false,
      },
      editing: {
        mode: 'row',
        allowUpdating: true,
        allowDeleting: true,
        allowAdding: true,
      },
      columns: [
        {
          dataField: 'Prefix',
          caption: 'Title',
        }, 'FirstName',
        'LastName', {
          dataField: 'Position',
          width: 130,
        }, {
          dataField: 'StateID',
          caption: 'State',
          width: 125,
          lookup: {
            dataSource: states,
            displayExpr: 'Name',
            valueExpr: 'ID',
          },
        }, {
          dataField: 'BirthDate',
          dataType: 'date',
          width: 125,
        },
      ],
      onEditingStart() {
        logEvent('EditingStart');
      },
      onInitNewRow() {
        logEvent('InitNewRow');
      },
      onRowInserting() {
        logEvent('RowInserting');
      },
      onRowInserted() {
        logEvent('RowInserted');
      },
      onRowUpdating() {
        logEvent('RowUpdating');
      },
      onRowUpdated() {
        logEvent('RowUpdated');
      },
      onRowRemoving() {
        logEvent('RowRemoving');
      },
      onRowRemoved() {
        logEvent('RowRemoved');
      },
      onSaving() {
        logEvent('Saving');
      },
      onSaved() {
        logEvent('Saved');
      },
      onEditCanceling() {
        logEvent('EditCanceling');
      },
      onEditCanceled() {
        logEvent('EditCanceled');
      },
    });
  
    $('#clear').dxButton({
      text: 'Clear',
      onClick() {
        $('#events ul').empty();
      },
    });
  });

  
  import React from 'react';
 
  import 'devextreme/dist/css/dx.light.css';
   
  import DataGrid, {
      Column,
      Editing,
      Form
  } from 'devextreme-react/data-grid';
  import { Item } from 'devextreme-react/form';
   
  class App extends React.Component {
      render() {
          return (
              <DataGrid>
                  <Editing
                      mode="form"
                      allowUpdating={true}>
                      <Form>
                          <Item itemType="group" caption="Personal Data">
                              <Item dataField="Prefix" />
                              <Item dataField="Full_Name" />
                              <Item dataField="Position" />
                              <Item dataField="Duties" editorType="dxTextArea" />
                          </Item>
                          <Item itemType="group" caption="Contacts">
                              <Item dataField="Email" />
                              <Item dataField="Skype" />
                          </Item>
                      </Form>
                  </Editing>
                  <Column dataField="Prefix" />
                  <Column dataField="Full_Name" />
                  <Column dataField="Position" />
                  <Column dataField="Duties" />
                  <Column dataField="Email" />
                  <Column dataField="Skype" />
              </DataGrid>
          );
      }
  }
  export default App;