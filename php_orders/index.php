<h1>Order List</h1>

<?php
$dbconn = pg_connect("host=db_order port=5432 dbname=postgres user=postgres password=postgres")or die("Could not connect");
$result = pg_query($dbconn, "SELECT * FROM orders_order");
?>
<table>
    <thead>
        <tr>
            <th>id</th>
			<th>description</th>
			<th>is_ready</th>
        </tr>
    </thead>
    <tbody>
<? 
while ( $row = pg_fetch_row($result) )
{

	echo '<tr>';
		echo '<td>' . $row[0] . '</td>';
		echo '<td>' . $row[1] . '</td>';
		echo '<td>' . ($row[2] ? 'true' : 'false') . '</td>';
	echo '</tr>';
}
?>
	</tbody>
</table>