var current_table = null
var selected_items = [];

function click_checkout() {
  document.getElementById('column_table').style.display = 'none'
  document.getElementById('column_menu_page').style.display = 'none'
}

function select_table(value) {
  current_table = value
  document.getElementById('column_table').style.display = 'none'
  document.getElementById('column_menu_page').style.display = 'flex'
  document.getElementById('item_display_column_title').innerHTML =
    'Table No: ' + current_table
}

function click_list_items(value) {
  document.getElementById('item_display_column_body').innerHTML = ''
  selected_items.push(JSON.parse(value.replace(/'/g, '"')))
  create_display()
}

function create_display() {
  var subtotal = 0
  var itemList = document.getElementById('item_display_column_body')
  for (var i = 0; i < selected_items.length; i++) {
    var item = selected_items[i]
    console.log(selected_items)
    var div = document.createElement('div')
    div.classList.add('item_display_column_body_row')
    subtotal = subtotal + item.price
    div.innerHTML =
      '<p>1 x <p/>' + '<p>' + item.name + '</p><p>$' + item.price + '</p>'
    itemList.appendChild(div)
  }
  document.getElementById('subtotal').innerHTML = 'Subtotal: $' + subtotal
  document.getElementById('check_out').style.display = 'block'
}