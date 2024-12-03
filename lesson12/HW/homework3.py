import logging
import xml.etree.ElementTree as ET


logging.basicConfig(filename='hw3.log', level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')


def find_incoming_by_group_number_from_file(file_path, group_number):

    try:
        tree = ET.parse(file_path)
        root = tree.getroot()

        for group in root.findall('group'):
            number = group.find('number')
            if number is not None and number.text == str(group_number):
                timing_exbytes = group.find('timingExbytes')
                if timing_exbytes is not None:
                    incoming = timing_exbytes.find('incoming')
                    if incoming is not None:
                        logging.info(f"Group {group_number}: incoming = {incoming.text}")
                        return incoming.text
        logging.info(f"Group {group_number} not found or has no incoming value.")
        return None

    except FileNotFoundError:
        logging.error(f"File not found: {file_path}")
        return None
    except ET.ParseError as e:
        logging.error(f"Error parsing XML file: {e}")
        return None


result_0 = find_incoming_by_group_number_from_file("groups.xml", 0)
result_2 = find_incoming_by_group_number_from_file("groups.xml", 2)
result_10 = find_incoming_by_group_number_from_file("groups.xml", 10)

