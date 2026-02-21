async function fetchData(table) {
    const res = await fetch(`/api/${table}`);
    return await res.json();
}
async function addData(table, data) {
    const res = await fetch(`/api/${table}`, {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify(data)
    });
    return await res.json();
}
async function updateData(table, id, data) {
    const res = await fetch(`/api/${table}/${id}`, {
        method: 'PUT',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify(data)
    });
    return await res.json();
}
async function deleteData(table, id) {
    const res = await fetch(`/api/${table}/${id}`, {
        method: 'DELETE'
    });
    return await res.json();
}
function handleFormSubmit(event, table, formId) {
    event.preventDefault();
    const form = document.getElementById(formId);
    const formData = new FormData(form);
    const data = Object.fromEntries(formData.entries());
    addData(table, data).then(() => {
        form.reset();
        refreshTable(table);
    });
}
function refreshTable(table) {
    fetchData(table).then(data => {
        const tbody = document.querySelector('tbody');
        if (!tbody) return;
        tbody.innerHTML = '';
        data.forEach(item => {
            const tr = document.createElement('tr');
            Object.keys(item).forEach(key => {
                if (key !== 'id') {
                    const td = document.createElement('td');
                    td.innerText = item[key];
                    tr.appendChild(td);
                }
            });
            const actionTd = document.createElement('td');
            const editBtn = document.createElement('button');
            editBtn.innerText = 'Edit';
            editBtn.onclick = () => updateRecord(table, item.id);
            const delBtn = document.createElement('button');
            delBtn.innerText = 'Delete';
            delBtn.onclick = () => {
                deleteData(table, item.id).then(() => refreshTable(table));
            };
            actionTd.appendChild(editBtn);
            actionTd.appendChild(delBtn);
            tr.appendChild(actionTd);
            tbody.appendChild(tr);
        });
    });
}
function updateRecord(table, id) {
    const newData = prompt("Enter new data as JSON:");
    if (newData) {
        try {
            const parsed = JSON.parse(newData);
            updateData(table, id, parsed).then(() => refreshTable(table));
        } catch (e) {
            alert("Invalid JSON");
        }
    }
}
