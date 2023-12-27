



-- Join 

-- 1 --

SELECT PetrolPump.Registration_No FROM PetrolPump INNER JOIN Employee ON PetrolPump.Registration_No = Employee.Petrolpump_No;

-- 2 --

SELECT Petrolpump.Registration_No FROM Petrolpump left join Employee on Petrolpump.Registration_No = Employee.Petrolpump_No WHERE Employee.Petrolpump_No is NULL;

-- 3 --

 SELECT PetrolPump.Registration_No FROM PetrolPump LEFT JOIN Employee ON PetrolPump.Registration_No = Employee.Petrolpump_No;

-- 4 --

SELECT Invoice.Invoice_No ,Invoice.Date ,Invoice.Payment_Type, Customer.C_Name , Customer.Phone_No FROM Invoice RIGHT OUTER JOIN Customer ON Customer.Customer_Code = Invoice.Customer_Code; 

--  Aggriate Functions 


-- 1 --
select avg(Age) from Customer where Gender='M';

-- 2 --

SELECT Emp_Name,TIMESTAMPDIFF(YEAR, DOB, CURDATE()) AS age FROM Employee;

--  3 --

SELECT * , max(Total_Price) FROM Invoice ;

-- 4 --

SELECT Sales_No, Sales_Amount, Petrolpump_No, max(Sales_Amount) FROM Sales WHERE DATE='2022-11-20';

--  SET Operations

--  1 --
 SELECT Owner_Name from Owners as Names UNION SELECT EMP_Name from Employee ;

-- 2 --
SELECT Registration_No from Petrolpump INTERSECT SELECT Petrolpump_No from Employee;

-- 3 --

  SELECT Petrolpump_Name FROM Petrolpump where Registration_No IN(SELECT Petrolpump.Registration_No FROM Petrolpump left join Employee on Petrolpump.Registration_No = Employee.Petrolpump_No WHERE Employee.Petrolpump_No is NULL);

--  4 --
SELECT  C_Name from Customer UNION SELECT Owner_Name from Owners;

--  Trigger --
DELIMITER $$
CREATE TRIGGER salary_check 
BEFORE UPDATE
ON Employee FOR EACH ROW
BEGIN
declare WAGE int(7);
declare error_msg varchar(225);
set error_msg = ("Error: Insufficient Salary For Living");
set WAGE = new.Salary;
if WAGE < 20000 then
signal sqlstate '45000'
set MESSAGE_TEXT = error_msg;
end if;
END $$
DELIMITER $$

CREATE PROCEDURE FindNearestPetrolPump(
    IN customer_latitude INT(3),
    IN customer_longitude INT(3)
)
BEGIN
    DECLARE min_distance DOUBLE;
    DECLARE nearest_pump_id INT;

    -- Initialize min_distance to a large value
    SET min_distance = 9999999999;

    -- Iterate over petrol pumps to find the nearest one
    SELECT PumpID, Latitude, Longitude
    INTO nearest_pump_id, @pump_latitude, @pump_longitude
    FROM Pumps;

    DECLARE done INT DEFAULT FALSE;
    DECLARE cur CURSOR FOR SELECT PumpID, Latitude, Longitude FROM Pumps;
    DECLARE CONTINUE HANDLER FOR NOT FOUND SET done = TRUE;

    OPEN cur;

    read_loop: LOOP
        FETCH cur INTO @current_pump_id, @current_latitude, @current_longitude;
        IF done THEN
            LEAVE read_loop;
        END IF;

        -- Calculate distance using a suitable formula (e.g., Haversine formula)
        SET @distance = 
            customer_latitude-@current_latitude + customer_longitude -
             @current_longitude
        ;

        -- Update nearest pump if the current one is closer
        IF @distance < min_distance THEN
            SET min_distance = @distance;
            SET nearest_pump_id = @current_pump_id;
            SET @pump_latitude = @current_latitude;
            SET @pump_longitude = @current_longitude;
        END IF;
    END LOOP;

    CLOSE cur;

    -- Return information about the nearest pump
    SELECT nearest_pump_id AS NearestPumpID, @pump_latitude AS Latitude, @pump_longitude AS Longitude, min_distance AS Distance;
END$$

DELIMITER ;

DELIMITER ;

--  to drop trigger 
drop trigger salary_check;

-- text 
UPDATE Employee SET Salary = 15000 WHERE Email_ID = "sheela@gmail.com";




-- Function 
DELIMITER $$
CREATE FUNCTION `TOTAL_AMOUNT`(`TID` VARCHAR(10)) RETURNS float
    DETERMINISTIC
BEGIN
	
    DECLARE BILL FLOAT;
    DECLARE RATE FLOAT;
    DECLARE VOL FLOAT;
    
    SET RATE = (SELECT FUEL_PRICE FROM TANKER WHERE TANKER_ID = TID);
    SET VOL = (SELECT FUEL_AMOUNT FROM TANKER WHERE TANKER_ID = TID);
    
    SET BILL = RATE * VOL;
    
    RETURN BILL;
    
END$$
DELIMITER ;

-- TO EXECUTE

SET @p0='BR6872'; SELECT `TOTAL_AMOUNT`(@p0) AS `TOTAL_AMOUNT`;

--  Procedure

DELIMITER $$
create procedure p()
begin
SELECT PetrolPump.Registration_No FROM PetrolPump INNER JOIN Employee ON PetrolPump.Registration_No = Employee.Petrolpump_No;
END $$

--  Modification --

DELIMITER $$
create procedure Modify()
begin
select total_sales, sales_amount from sales where month(date) = 11;
END $$
DELIMITER $$

CREATE PROCEDURE NearestPetrolPumps(
    IN customer_latitude DECIMAL(9, 6),
    IN customer_longitude DECIMAL(9, 6)
)

BEGIN
    SELECT
        Petrolpump_Name as Petrolpump_Name,
        Latitude as Latitude,
        Longitude as Longitude,
        EuclideanDistance(
            customer_latitude, customer_longitude,
            Latitude, Longitude
        ) AS Distance
    FROM PetrolPump
    ORDER BY Distance;
END $$

DELIMITER ;
set global log_bin_trust_function_creators=1;
DELIMITER $$

CREATE FUNCTION EuclideanDistance(
    x1 DECIMAL(9, 6),
    y1 DECIMAL(9, 6),
    x2 DECIMAL(9, 6),
    y2 DECIMAL(9, 6)
) RETURNS DECIMAL(10, 2)
BEGIN
    DECLARE distance DECIMAL(10, 2);
    
    SET distance = SQRT(POW(x2 - x1, 2) + POW(y2 - y1, 2));
    
    RETURN distance;
END $$
  
DELIMITER ;

DELIMITER $$

CREATE PROCEDURE FindMostRushIntervalForPetrolPump(
    IN pump_id varchar(10)
)
BEGIN
    DECLARE most_rush_interval VARCHAR(20);

    SELECT 
        CASE 
            WHEN HOUR(Time_Interval) BETWEEN 6 AND 12 THEN 'Morning'
            WHEN HOUR(Time_interval) BETWEEN 12 AND 18 THEN 'Afternoon'
            ELSE 'Evening/Night'
        END AS RushInterval,
        COUNT(*) AS TransactionCount
    INTO
        most_rush_interval
    FROM 
        Sales
    WHERE 
        Petrolpump_No = pump_id
    GROUP BY 
        RushInterval
    ORDER BY 
        TransactionCount DESC
    LIMIT 1;

    SELECT most_rush_interval AS MostRushInterval;
END $$

DELIMITER ;


