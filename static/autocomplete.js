document.addEventListener('DOMContentLoaded', function() {
    const searchInput = document.getElementById('player-search');
    const dropdown = document.getElementById('autocomplete-dropdown');
    let currentFocus = -1;

    searchInput.addEventListener('input', function() {
        const query = this.value;
        
        if (query.length < 2) {
            dropdown.innerHTML = '';
            dropdown.style.display = 'none';
            return;
        }

        fetch(`/api/players?q=${encodeURIComponent(query)}`)
            .then(response => response.json())
            .then(players => {
                dropdown.innerHTML = '';
                
                if (players.length > 0) {
                    players.forEach((player, index) => {
                        const div = document.createElement('div');
                        div.className = 'autocomplete-item';
                        div.textContent = player;
                        div.addEventListener('click', function() {
                            searchInput.value = player;
                            dropdown.innerHTML = '';
                            dropdown.style.display = 'none';
                        });
                        dropdown.appendChild(div);
                    });
                    dropdown.style.display = 'block';
                } else {
                    dropdown.style.display = 'none';
                }
            })
            .catch(error => {
                console.error('Error fetching players:', error);
                dropdown.style.display = 'none';
            });
    });

    document.addEventListener('click', function(e) {
        if (!searchInput.contains(e.target) && !dropdown.contains(e.target)) {
            dropdown.style.display = 'none';
        }
    });

    searchInput.addEventListener('keydown', function(e) {
        const items = dropdown.querySelectorAll('.autocomplete-item');
        
        if (e.key === 'ArrowDown') {
            e.preventDefault();
            currentFocus++;
            if (currentFocus >= items.length) currentFocus = 0;
            setActive(items);
        } else if (e.key === 'ArrowUp') {
            e.preventDefault();
            currentFocus--;
            if (currentFocus < 0) currentFocus = items.length - 1;
            setActive(items);
        } else if (e.key === 'Enter') {
            e.preventDefault();
            if (currentFocus > -1 && items[currentFocus]) {
                searchInput.value = items[currentFocus].textContent;
                dropdown.style.display = 'none';
            }
        }
    });

    function setActive(items) {
        items.forEach((item, index) => {
            item.classList.toggle('autocomplete-active', index === currentFocus);
        });
    }
});