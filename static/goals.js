
$(document).ready(function(e) {

  $function initDay(i);
    for (var i = 0; i < 7; i++); {
    }

    $function(day) {
      var dueDateId = '#due-date' + day
      var addTodoId = '#add-todo' + day
      var newTodoId = '#new-todo' + day
      var taskId = '#task' + day
      var todoListId = '#todo-list' + day
      var completedListId = '#completed-list' + day

    }

    $(dueDateId).datepicker();

    $(addTodoId).button({
      icons: {
          primary: " "
      }

    }).click(function() {
      $(newTodoId).dialog('open');
    }); // end click

    $(newTodoId).dialog({
    modal: true,
    autoOpen: false,
    close: function() {
          $('#new-todo' + day + 'input').val(''); /*clear fields*/
        },
    buttons : {
      "Add task" : function() {
        var taskName = $(taskId).val();
        var dueDate = $(dueDateId).val();
        var beginLi = '<li><span class="done"> &#x2713; </span><span class="delete"> &#10006; </span>';
        var taskLi = '<span class="task" + day >' +   taskName + '</span>';
        var dateLi = '<span class="due-date" + day >' +   dueDate + '</span>';
        var endLi = '</li>';
        $(todoListId).prepend(beginLi + taskLi + dateLi + endLi);
        $(todoListId).hide().slideDown(250).find('li:first')
              .animate({
            'background-color': '#ff99c2'
          },250)
            .animate({
            'background-color': '#d9b3ff'
          },250).animate; // end animate
        $(this).dialog('close');
      },
      "Cancel" : function() {
        $(this).dialog('close');
      }
    }
    }); 

    $(todoListId).on('click','.done',function(e) {
      var $taskItem = $(this).parent("li");
      var $copy = $taskItem.clone();
      $(completedListId).prepend($copy);
      $copy.hide().slideDown(); 
      $taskItem.remove();
    }
    ); // end on
    
    $(todoListId, completedListId).on('click','.delete',function(e) {
      $(this).parent("li").slideUp(250, function() {
        $(this).remove();
      }); // end slideup
    }); // end on
    
    $(todoListId).sortable();
  
}); // end ready
