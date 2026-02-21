const table = document.getElementById("table").innerHTML;

table = `
            <table>
                <thead>
                    <tr>
                        <th>Vehicle ID</th>
                        <th>Type</th>
                        <th>Driver</th>
                        <th>Region</th>
                        <th>Status</th>
                    </tr>
                </thead>
                <tbody>
                    <tr>
                        <td>TRK-001</td>
                        <td>Heavy Truck</td>
                        <td>John Doe</td>
                        <td>North</td>
                        <td><span class="status-badge status-trip">On Trip</span></td>
                    </tr>
                    <tr>
                        <td>VAN-042</td>
                        <td>Delivery Van</td>
                        <td>Sarah Smith</td>
                        <td>East</td>
                        <td><span class="status-badge status-idle">Idle</span></td>
                    </tr>
                    <tr>
                        <td>TRK-012</td>
                        <td>Heavy Truck</td>
                        <td>Mike Ross</td>
                        <td>West</td>
                        <td><span class="status-badge status-shop">In Shop</span></td>
                    </tr>
                    <tr>
                        <td>BIKE-09</td>
                        <td>Bike/Courier</td>
                        <td>Jessica Lee</td>
                        <td>South</td>
                        <td><span class="status-badge status-trip">On Trip</span></td>
                    </tr>
                </tbody>
            </table>`

