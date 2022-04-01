import sgqlc.types
import sgqlc.types.datetime
import sgqlc.types.relay


shiphero_schema = sgqlc.types.Schema()


# Unexport Node/PageInfo, let schema re-declare them
shiphero_schema -= sgqlc.types.relay.Node
shiphero_schema -= sgqlc.types.relay.PageInfo


__docformat__ = 'markdown'


########################################################################
# Scalars and Enumerations
########################################################################
Boolean = sgqlc.types.Boolean

Date = sgqlc.types.datetime.Date

class Decimal(sgqlc.types.Scalar):
    __schema__ = shiphero_schema


class EntityType(sgqlc.types.Enum):
    '''Enumeration Choices:

    * `Account`
    * `Bin`
    * `LineItem`
    * `LocationType`
    * `Order`
    * `Product`
    * `PurchaseOrder`
    * `PurchaseOrderLineItem`
    * `Return`
    * `ReturnItem`
    * `Shipment`
    * `ShippedLineItem`
    * `Tote`
    * `User`
    * `Vendor`
    * `Warehouse`
    * `WarehouseProduct`
    '''
    __schema__ = shiphero_schema
    __choices__ = ('Account', 'Bin', 'LineItem', 'LocationType', 'Order', 'Product', 'PurchaseOrder', 'PurchaseOrderLineItem', 'Return', 'ReturnItem', 'Shipment', 'ShippedLineItem', 'Tote', 'User', 'Vendor', 'Warehouse', 'WarehouseProduct')


class GenericScalar(sgqlc.types.Scalar):
    __schema__ = shiphero_schema


ID = sgqlc.types.ID

class ISODateTime(sgqlc.types.Scalar):
    __schema__ = shiphero_schema


Int = sgqlc.types.Int

class Money(sgqlc.types.Scalar):
    __schema__ = shiphero_schema


class ReturnLabelType(sgqlc.types.Enum):
    '''Enumeration Choices:

    * `FLAT_RATE`
    * `FREE`
    * `PAID`
    * `SELF_RETURN`
    '''
    __schema__ = shiphero_schema
    __choices__ = ('FLAT_RATE', 'FREE', 'PAID', 'SELF_RETURN')


String = sgqlc.types.String


########################################################################
# Input Objects
########################################################################
class AbortInventorySyncInput(sgqlc.types.Input):
    __schema__ = shiphero_schema
    __field_names__ = ('sync_id', 'reason')
    sync_id = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='sync_id')

    reason = sgqlc.types.Field(String, graphql_name='reason')



class AddHistoryInput(sgqlc.types.Input):
    __schema__ = shiphero_schema
    __field_names__ = ('customer_account_id', 'order_id', 'history_entry')
    customer_account_id = sgqlc.types.Field(String, graphql_name='customer_account_id')

    order_id = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='order_id')

    history_entry = sgqlc.types.Field('UserNoteInput', graphql_name='history_entry')



class AddLineItemsInput(sgqlc.types.Input):
    __schema__ = shiphero_schema
    __field_names__ = ('customer_account_id', 'order_id', 'line_items')
    customer_account_id = sgqlc.types.Field(String, graphql_name='customer_account_id')

    order_id = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='order_id')

    line_items = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of('CreateLineItemInput')), graphql_name='line_items')



class AddProductToVendorInput(sgqlc.types.Input):
    __schema__ = shiphero_schema
    __field_names__ = ('customer_account_id', 'vendor_id', 'sku', 'manufacturer_sku', 'price')
    customer_account_id = sgqlc.types.Field(String, graphql_name='customer_account_id')

    vendor_id = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='vendor_id')

    sku = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='sku')

    manufacturer_sku = sgqlc.types.Field(String, graphql_name='manufacturer_sku')

    price = sgqlc.types.Field(String, graphql_name='price')



class AddProductToWarehouseInput(sgqlc.types.Input):
    __schema__ = shiphero_schema
    __field_names__ = ('customer_account_id', 'sku', 'warehouse_id', 'on_hand', 'inventory_bin', 'inventory_overstock_bin', 'reserve_inventory', 'replenishment_level', 'reorder_level', 'reorder_amount', 'price')
    customer_account_id = sgqlc.types.Field(String, graphql_name='customer_account_id')

    sku = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='sku')

    warehouse_id = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='warehouse_id')

    on_hand = sgqlc.types.Field(Int, graphql_name='on_hand')

    inventory_bin = sgqlc.types.Field(String, graphql_name='inventory_bin')

    inventory_overstock_bin = sgqlc.types.Field(String, graphql_name='inventory_overstock_bin')

    reserve_inventory = sgqlc.types.Field(Int, graphql_name='reserve_inventory')

    replenishment_level = sgqlc.types.Field(Int, graphql_name='replenishment_level')

    reorder_level = sgqlc.types.Field(Int, graphql_name='reorder_level')

    reorder_amount = sgqlc.types.Field(Int, graphql_name='reorder_amount')

    price = sgqlc.types.Field(String, graphql_name='price')



class AddPurchaseOrderAttachmentInput(sgqlc.types.Input):
    __schema__ = shiphero_schema
    __field_names__ = ('po_id', 'url', 'description', 'filename', 'file_type')
    po_id = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='po_id')

    url = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='url')

    description = sgqlc.types.Field(String, graphql_name='description')

    filename = sgqlc.types.Field(String, graphql_name='filename')

    file_type = sgqlc.types.Field(String, graphql_name='file_type')



class AddressInput(sgqlc.types.Input):
    __schema__ = shiphero_schema
    __field_names__ = ('name', 'address1', 'address2', 'city', 'state', 'country', 'zip', 'phone')
    name = sgqlc.types.Field(String, graphql_name='name')

    address1 = sgqlc.types.Field(String, graphql_name='address1')

    address2 = sgqlc.types.Field(String, graphql_name='address2')

    city = sgqlc.types.Field(String, graphql_name='city')

    state = sgqlc.types.Field(String, graphql_name='state')

    country = sgqlc.types.Field(String, graphql_name='country')

    zip = sgqlc.types.Field(String, graphql_name='zip')

    phone = sgqlc.types.Field(String, graphql_name='phone')



class AssignLotToLocationInput(sgqlc.types.Input):
    __schema__ = shiphero_schema
    __field_names__ = ('lot_id', 'location_id')
    lot_id = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='lot_id')

    location_id = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='location_id')



class BuildKitComponentInput(sgqlc.types.Input):
    __schema__ = shiphero_schema
    __field_names__ = ('sku', 'quantity')
    sku = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='sku')

    quantity = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='quantity')



class BuildKitInput(sgqlc.types.Input):
    __schema__ = shiphero_schema
    __field_names__ = ('sku', 'components', 'kit_build', 'warehouse_id')
    sku = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='sku')

    components = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(BuildKitComponentInput)), graphql_name='components')

    kit_build = sgqlc.types.Field(Boolean, graphql_name='kit_build')

    warehouse_id = sgqlc.types.Field(String, graphql_name='warehouse_id')



class CancelOrderInput(sgqlc.types.Input):
    __schema__ = shiphero_schema
    __field_names__ = ('customer_account_id', 'order_id', 'reason', 'void_on_platform', 'force')
    customer_account_id = sgqlc.types.Field(String, graphql_name='customer_account_id')

    order_id = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='order_id')

    reason = sgqlc.types.Field(String, graphql_name='reason')

    void_on_platform = sgqlc.types.Field(Boolean, graphql_name='void_on_platform')

    force = sgqlc.types.Field(Boolean, graphql_name='force')



class CancelPurchaseOrderInput(sgqlc.types.Input):
    __schema__ = shiphero_schema
    __field_names__ = ('customer_account_id', 'po_id')
    customer_account_id = sgqlc.types.Field(String, graphql_name='customer_account_id')

    po_id = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='po_id')



class ChangeOrderWarehouseInput(sgqlc.types.Input):
    __schema__ = shiphero_schema
    __field_names__ = ('customer_account_id', 'order_id', 'warehouse_id')
    customer_account_id = sgqlc.types.Field(String, graphql_name='customer_account_id')

    order_id = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='order_id')

    warehouse_id = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='warehouse_id')



class ClearKitInput(sgqlc.types.Input):
    __schema__ = shiphero_schema
    __field_names__ = ('customer_account_id', 'sku')
    customer_account_id = sgqlc.types.Field(String, graphql_name='customer_account_id')

    sku = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='sku')



class ClosePurchaseOrderInput(sgqlc.types.Input):
    __schema__ = shiphero_schema
    __field_names__ = ('customer_account_id', 'po_id')
    customer_account_id = sgqlc.types.Field(String, graphql_name='customer_account_id')

    po_id = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='po_id')



class CreateBillInput(sgqlc.types.Input):
    __schema__ = shiphero_schema
    __field_names__ = ('customer_account_id', 'start_date', 'end_date')
    customer_account_id = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='customer_account_id')

    start_date = sgqlc.types.Field(sgqlc.types.non_null(ISODateTime), graphql_name='start_date')

    end_date = sgqlc.types.Field(sgqlc.types.non_null(ISODateTime), graphql_name='end_date')



class CreateExchangeItem(sgqlc.types.Input):
    __schema__ = shiphero_schema
    __field_names__ = ('return_item_id', 'exchange_product_sku', 'quantity')
    return_item_id = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='return_item_id')

    exchange_product_sku = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='exchange_product_sku')

    quantity = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='quantity')



class CreateLabelResourceInput(sgqlc.types.Input):
    __schema__ = shiphero_schema
    __field_names__ = ('paper_pdf_location', 'thermal_pdf_location', 'pdf_location', 'image_location')
    paper_pdf_location = sgqlc.types.Field(String, graphql_name='paper_pdf_location')

    thermal_pdf_location = sgqlc.types.Field(String, graphql_name='thermal_pdf_location')

    pdf_location = sgqlc.types.Field(String, graphql_name='pdf_location')

    image_location = sgqlc.types.Field(String, graphql_name='image_location')



class CreateLineItemInput(sgqlc.types.Input):
    __schema__ = shiphero_schema
    __field_names__ = ('sku', 'partner_line_item_id', 'quantity', 'price', 'product_name', 'option_title', 'fulfillment_status', 'quantity_pending_fulfillment', 'custom_options', 'custom_barcode', 'eligible_for_return', 'customs_value', 'barcode', 'warehouse_id')
    sku = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='sku')

    partner_line_item_id = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='partner_line_item_id')

    quantity = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='quantity')

    price = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='price')

    product_name = sgqlc.types.Field(String, graphql_name='product_name')

    option_title = sgqlc.types.Field(String, graphql_name='option_title')

    fulfillment_status = sgqlc.types.Field(String, graphql_name='fulfillment_status')

    quantity_pending_fulfillment = sgqlc.types.Field(Int, graphql_name='quantity_pending_fulfillment')

    custom_options = sgqlc.types.Field(GenericScalar, graphql_name='custom_options')

    custom_barcode = sgqlc.types.Field(String, graphql_name='custom_barcode')

    eligible_for_return = sgqlc.types.Field(Boolean, graphql_name='eligible_for_return')

    customs_value = sgqlc.types.Field(String, graphql_name='customs_value')

    barcode = sgqlc.types.Field(String, graphql_name='barcode')

    warehouse_id = sgqlc.types.Field(String, graphql_name='warehouse_id')



class CreateLocationInput(sgqlc.types.Input):
    __schema__ = shiphero_schema
    __field_names__ = ('warehouse_id', 'name', 'zone', 'location_type_id', 'pickable', 'sellable', 'is_cart', 'pick_priority', 'dimensions', 'temperature')
    warehouse_id = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='warehouse_id')

    name = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='name')

    zone = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='zone')

    location_type_id = sgqlc.types.Field(String, graphql_name='location_type_id')

    pickable = sgqlc.types.Field(Boolean, graphql_name='pickable')

    sellable = sgqlc.types.Field(Boolean, graphql_name='sellable')

    is_cart = sgqlc.types.Field(Boolean, graphql_name='is_cart')

    pick_priority = sgqlc.types.Field(Int, graphql_name='pick_priority')

    dimensions = sgqlc.types.Field('DimensionsInput', graphql_name='dimensions')

    temperature = sgqlc.types.Field(String, graphql_name='temperature')



class CreateLotInput(sgqlc.types.Input):
    __schema__ = shiphero_schema
    __field_names__ = ('customer_account_id', 'name', 'sku', 'expires_at', 'is_active')
    customer_account_id = sgqlc.types.Field(String, graphql_name='customer_account_id')

    name = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='name')

    sku = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='sku')

    expires_at = sgqlc.types.Field(ISODateTime, graphql_name='expires_at')

    is_active = sgqlc.types.Field(Boolean, graphql_name='is_active')



class CreateOrderAddressInput(sgqlc.types.Input):
    __schema__ = shiphero_schema
    __field_names__ = ('first_name', 'last_name', 'company', 'address1', 'address2', 'city', 'state', 'state_code', 'zip', 'country', 'country_code', 'email', 'phone')
    first_name = sgqlc.types.Field(String, graphql_name='first_name')

    last_name = sgqlc.types.Field(String, graphql_name='last_name')

    company = sgqlc.types.Field(String, graphql_name='company')

    address1 = sgqlc.types.Field(String, graphql_name='address1')

    address2 = sgqlc.types.Field(String, graphql_name='address2')

    city = sgqlc.types.Field(String, graphql_name='city')

    state = sgqlc.types.Field(String, graphql_name='state')

    state_code = sgqlc.types.Field(String, graphql_name='state_code')

    zip = sgqlc.types.Field(String, graphql_name='zip')

    country = sgqlc.types.Field(String, graphql_name='country')

    country_code = sgqlc.types.Field(String, graphql_name='country_code')

    email = sgqlc.types.Field(String, graphql_name='email')

    phone = sgqlc.types.Field(String, graphql_name='phone')



class CreateOrderInput(sgqlc.types.Input):
    __schema__ = shiphero_schema
    __field_names__ = ('customer_account_id', 'order_number', 'partner_order_id', 'shop_name', 'fulfillment_status', 'order_date', 'total_tax', 'subtotal', 'total_discounts', 'total_price', 'box_name', 'currency', 'ready_to_ship', 'shipping_lines', 'shipping_address', 'billing_address', 'from_name', 'note_attributes', 'tags', 'line_items', 'gift_note', 'gift_invoice', 'require_signature', 'adult_signature_required', 'alcohol', 'insurance', 'allow_partial', 'allow_split', 'custom_invoice_url', 'email', 'profile', 'packing_note', 'required_ship_date', 'auto_print_return_label', 'hold_until_date', 'incoterms', 'tax_id', 'tax_type', 'flagged', 'saturday_delivery', 'ignore_address_validation_errors', 'skip_address_validation', 'priority_flag', 'allocation_priority', 'holds', 'dry_ice_weight_in_lbs', 'ftr_exemption', 'address_is_business')
    customer_account_id = sgqlc.types.Field(String, graphql_name='customer_account_id')

    order_number = sgqlc.types.Field(String, graphql_name='order_number')

    partner_order_id = sgqlc.types.Field(String, graphql_name='partner_order_id')

    shop_name = sgqlc.types.Field(String, graphql_name='shop_name')

    fulfillment_status = sgqlc.types.Field(String, graphql_name='fulfillment_status')

    order_date = sgqlc.types.Field(ISODateTime, graphql_name='order_date')

    total_tax = sgqlc.types.Field(String, graphql_name='total_tax')

    subtotal = sgqlc.types.Field(String, graphql_name='subtotal')

    total_discounts = sgqlc.types.Field(String, graphql_name='total_discounts')

    total_price = sgqlc.types.Field(String, graphql_name='total_price')

    box_name = sgqlc.types.Field(String, graphql_name='box_name')

    currency = sgqlc.types.Field(String, graphql_name='currency')

    ready_to_ship = sgqlc.types.Field(Boolean, graphql_name='ready_to_ship')

    shipping_lines = sgqlc.types.Field('CreateShippingLinesInput', graphql_name='shipping_lines')

    shipping_address = sgqlc.types.Field(sgqlc.types.non_null(CreateOrderAddressInput), graphql_name='shipping_address')

    billing_address = sgqlc.types.Field(CreateOrderAddressInput, graphql_name='billing_address')

    from_name = sgqlc.types.Field(String, graphql_name='from_name')

    note_attributes = sgqlc.types.Field(sgqlc.types.list_of('OrderNoteAttributeInput'), graphql_name='note_attributes')

    tags = sgqlc.types.Field(sgqlc.types.list_of(String), graphql_name='tags')

    line_items = sgqlc.types.Field(sgqlc.types.list_of(CreateLineItemInput), graphql_name='line_items')

    gift_note = sgqlc.types.Field(String, graphql_name='gift_note')

    gift_invoice = sgqlc.types.Field(Boolean, graphql_name='gift_invoice')

    require_signature = sgqlc.types.Field(Boolean, graphql_name='require_signature')

    adult_signature_required = sgqlc.types.Field(Boolean, graphql_name='adult_signature_required')

    alcohol = sgqlc.types.Field(Boolean, graphql_name='alcohol')

    insurance = sgqlc.types.Field(Boolean, graphql_name='insurance')

    allow_partial = sgqlc.types.Field(Boolean, graphql_name='allow_partial')

    allow_split = sgqlc.types.Field(Boolean, graphql_name='allow_split')

    custom_invoice_url = sgqlc.types.Field(String, graphql_name='custom_invoice_url')

    email = sgqlc.types.Field(String, graphql_name='email')

    profile = sgqlc.types.Field(String, graphql_name='profile')

    packing_note = sgqlc.types.Field(String, graphql_name='packing_note')

    required_ship_date = sgqlc.types.Field(ISODateTime, graphql_name='required_ship_date')

    auto_print_return_label = sgqlc.types.Field(Boolean, graphql_name='auto_print_return_label')

    hold_until_date = sgqlc.types.Field(ISODateTime, graphql_name='hold_until_date')

    incoterms = sgqlc.types.Field(String, graphql_name='incoterms')

    tax_id = sgqlc.types.Field(String, graphql_name='tax_id')

    tax_type = sgqlc.types.Field(String, graphql_name='tax_type')

    flagged = sgqlc.types.Field(Boolean, graphql_name='flagged')

    saturday_delivery = sgqlc.types.Field(Boolean, graphql_name='saturday_delivery')

    ignore_address_validation_errors = sgqlc.types.Field(Boolean, graphql_name='ignore_address_validation_errors')

    skip_address_validation = sgqlc.types.Field(Boolean, graphql_name='skip_address_validation')

    priority_flag = sgqlc.types.Field(Boolean, graphql_name='priority_flag')

    allocation_priority = sgqlc.types.Field(Int, graphql_name='allocation_priority')

    holds = sgqlc.types.Field('HoldsInput', graphql_name='holds')

    dry_ice_weight_in_lbs = sgqlc.types.Field(String, graphql_name='dry_ice_weight_in_lbs')

    ftr_exemption = sgqlc.types.Field(Decimal, graphql_name='ftr_exemption')

    address_is_business = sgqlc.types.Field(Boolean, graphql_name='address_is_business')



class CreateProductImageInput(sgqlc.types.Input):
    __schema__ = shiphero_schema
    __field_names__ = ('src', 'position')
    src = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='src')

    position = sgqlc.types.Field(Int, graphql_name='position')



class CreateProductInput(sgqlc.types.Input):
    __schema__ = shiphero_schema
    __field_names__ = ('customer_account_id', 'name', 'sku', 'price', 'value', 'warehouse_products', 'barcode', 'country_of_manufacture', 'dimensions', 'tariff_code', 'kit', 'kit_build', 'no_air', 'final_sale', 'customs_value', 'customs_description', 'not_owned', 'dropship', 'needs_serial_number', 'virtual', 'needs_lot_tracking', 'images', 'tags', 'vendors', 'packer_note')
    customer_account_id = sgqlc.types.Field(String, graphql_name='customer_account_id')

    name = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='name')

    sku = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='sku')

    price = sgqlc.types.Field(String, graphql_name='price')

    value = sgqlc.types.Field(String, graphql_name='value')

    warehouse_products = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of('CreateWarehouseProductInput')), graphql_name='warehouse_products')

    barcode = sgqlc.types.Field(String, graphql_name='barcode')

    country_of_manufacture = sgqlc.types.Field(String, graphql_name='country_of_manufacture')

    dimensions = sgqlc.types.Field('DimensionsInput', graphql_name='dimensions')

    tariff_code = sgqlc.types.Field(String, graphql_name='tariff_code')

    kit = sgqlc.types.Field(Boolean, graphql_name='kit')

    kit_build = sgqlc.types.Field(Boolean, graphql_name='kit_build')

    no_air = sgqlc.types.Field(Boolean, graphql_name='no_air')

    final_sale = sgqlc.types.Field(Boolean, graphql_name='final_sale')

    customs_value = sgqlc.types.Field(String, graphql_name='customs_value')

    customs_description = sgqlc.types.Field(String, graphql_name='customs_description')

    not_owned = sgqlc.types.Field(Boolean, graphql_name='not_owned')

    dropship = sgqlc.types.Field(Boolean, graphql_name='dropship')

    needs_serial_number = sgqlc.types.Field(Boolean, graphql_name='needs_serial_number')

    virtual = sgqlc.types.Field(Boolean, graphql_name='virtual')

    needs_lot_tracking = sgqlc.types.Field(Boolean, graphql_name='needs_lot_tracking')

    images = sgqlc.types.Field(sgqlc.types.list_of(CreateProductImageInput), graphql_name='images')

    tags = sgqlc.types.Field(sgqlc.types.list_of(String), graphql_name='tags')

    vendors = sgqlc.types.Field(sgqlc.types.list_of('CreateProductVendorInput'), graphql_name='vendors')

    packer_note = sgqlc.types.Field(String, graphql_name='packer_note')



class CreateProductVendorInput(sgqlc.types.Input):
    __schema__ = shiphero_schema
    __field_names__ = ('vendor_id', 'vendor_sku', 'price')
    vendor_id = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='vendor_id')

    vendor_sku = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='vendor_sku')

    price = sgqlc.types.Field(String, graphql_name='price')



class CreatePurchaseOrderAttachmentInput(sgqlc.types.Input):
    __schema__ = shiphero_schema
    __field_names__ = ('url', 'description', 'filename', 'file_type')
    url = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='url')

    description = sgqlc.types.Field(String, graphql_name='description')

    filename = sgqlc.types.Field(String, graphql_name='filename')

    file_type = sgqlc.types.Field(String, graphql_name='file_type')



class CreatePurchaseOrderInput(sgqlc.types.Input):
    __schema__ = shiphero_schema
    __field_names__ = ('customer_account_id', 'po_number', 'subtotal', 'shipping_price', 'total_price', 'warehouse_id', 'line_items', 'po_date', 'po_note', 'fulfillment_status', 'discount', 'vendor_id', 'warehouse', 'packing_note', 'description', 'partner_order_number', 'tax', 'tracking_number', 'attachments', 'origin_of_shipment')
    customer_account_id = sgqlc.types.Field(String, graphql_name='customer_account_id')

    po_number = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='po_number')

    subtotal = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='subtotal')

    shipping_price = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='shipping_price')

    total_price = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='total_price')

    warehouse_id = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='warehouse_id')

    line_items = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of('CreatePurchaseOrderLineItemInput')), graphql_name='line_items')

    po_date = sgqlc.types.Field(ISODateTime, graphql_name='po_date')

    po_note = sgqlc.types.Field(String, graphql_name='po_note')

    fulfillment_status = sgqlc.types.Field(String, graphql_name='fulfillment_status')

    discount = sgqlc.types.Field(String, graphql_name='discount')

    vendor_id = sgqlc.types.Field(String, graphql_name='vendor_id')

    warehouse = sgqlc.types.Field(String, graphql_name='warehouse')

    packing_note = sgqlc.types.Field(String, graphql_name='packing_note')

    description = sgqlc.types.Field(String, graphql_name='description')

    partner_order_number = sgqlc.types.Field(String, graphql_name='partner_order_number')

    tax = sgqlc.types.Field(String, graphql_name='tax')

    tracking_number = sgqlc.types.Field(String, graphql_name='tracking_number')

    attachments = sgqlc.types.Field(sgqlc.types.list_of(CreatePurchaseOrderAttachmentInput), graphql_name='attachments')

    origin_of_shipment = sgqlc.types.Field(String, graphql_name='origin_of_shipment')



class CreatePurchaseOrderLineItemInput(sgqlc.types.Input):
    __schema__ = shiphero_schema
    __field_names__ = ('sku', 'quantity', 'expected_weight_in_lbs', 'price', 'vendor_id', 'vendor_sku', 'variant_id', 'quantity_received', 'quantity_rejected', 'product_name', 'option_title', 'fulfillment_status', 'sell_ahead', 'note', 'partner_line_item_id')
    sku = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='sku')

    quantity = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='quantity')

    expected_weight_in_lbs = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='expected_weight_in_lbs')

    price = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='price')

    vendor_id = sgqlc.types.Field(String, graphql_name='vendor_id')

    vendor_sku = sgqlc.types.Field(String, graphql_name='vendor_sku')

    variant_id = sgqlc.types.Field(Int, graphql_name='variant_id')

    quantity_received = sgqlc.types.Field(Int, graphql_name='quantity_received')

    quantity_rejected = sgqlc.types.Field(Int, graphql_name='quantity_rejected')

    product_name = sgqlc.types.Field(String, graphql_name='product_name')

    option_title = sgqlc.types.Field(String, graphql_name='option_title')

    fulfillment_status = sgqlc.types.Field(String, graphql_name='fulfillment_status')

    sell_ahead = sgqlc.types.Field(Int, graphql_name='sell_ahead')

    note = sgqlc.types.Field(String, graphql_name='note')

    partner_line_item_id = sgqlc.types.Field(String, graphql_name='partner_line_item_id')



class CreateReturnExchangeInput(sgqlc.types.Input):
    __schema__ = shiphero_schema
    __field_names__ = ('customer_account_id', 'return_id', 'exchange_items')
    customer_account_id = sgqlc.types.Field(String, graphql_name='customer_account_id')

    return_id = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='return_id')

    exchange_items = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(CreateExchangeItem)), graphql_name='exchange_items')



class CreateReturnInput(sgqlc.types.Input):
    __schema__ = shiphero_schema
    __field_names__ = ('customer_account_id', 'order_id', 'warehouse_id', 'return_reason', 'label_type', 'label_cost', 'address', 'dimensions', 'shipping_carrier', 'shipping_method', 'line_items', 'tracking_number', 'create_label', 'partner_id', 'display_issue_refund')
    customer_account_id = sgqlc.types.Field(String, graphql_name='customer_account_id')

    order_id = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='order_id')

    warehouse_id = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='warehouse_id')

    return_reason = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='return_reason')

    label_type = sgqlc.types.Field(sgqlc.types.non_null(ReturnLabelType), graphql_name='label_type')

    label_cost = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='label_cost')

    address = sgqlc.types.Field(sgqlc.types.non_null(AddressInput), graphql_name='address')

    dimensions = sgqlc.types.Field(sgqlc.types.non_null('DimensionsInput'), graphql_name='dimensions')

    shipping_carrier = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='shipping_carrier')

    shipping_method = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='shipping_method')

    line_items = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of('CreateReturnLineItemInput')), graphql_name='line_items')

    tracking_number = sgqlc.types.Field(String, graphql_name='tracking_number')

    create_label = sgqlc.types.Field(Boolean, graphql_name='create_label')

    partner_id = sgqlc.types.Field(String, graphql_name='partner_id')

    display_issue_refund = sgqlc.types.Field(Boolean, graphql_name='display_issue_refund')



class CreateReturnItemExchangeInput(sgqlc.types.Input):
    __schema__ = shiphero_schema
    __field_names__ = ('exchange_product_sku', 'quantity')
    exchange_product_sku = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='exchange_product_sku')

    quantity = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='quantity')



class CreateReturnLineItemInput(sgqlc.types.Input):
    __schema__ = shiphero_schema
    __field_names__ = ('sku', 'quantity', 'return_reason', 'condition', 'is_component', 'exchange_items')
    sku = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='sku')

    quantity = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='quantity')

    return_reason = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='return_reason')

    condition = sgqlc.types.Field(String, graphql_name='condition')

    is_component = sgqlc.types.Field(Boolean, graphql_name='is_component')

    exchange_items = sgqlc.types.Field(sgqlc.types.list_of(CreateReturnItemExchangeInput), graphql_name='exchange_items')



class CreateShipmentInput(sgqlc.types.Input):
    __schema__ = shiphero_schema
    __field_names__ = ('customer_account_id', 'order_id', 'warehouse_id', 'address', 'line_items', 'labels', 'notify_customer_via_shiphero', 'notify_customer_via_store', 'shipped_off_shiphero', 'profile')
    customer_account_id = sgqlc.types.Field(String, graphql_name='customer_account_id')

    order_id = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='order_id')

    warehouse_id = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='warehouse_id')

    address = sgqlc.types.Field(sgqlc.types.non_null(AddressInput), graphql_name='address')

    line_items = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of('CreateShipmentLineItemInput')), graphql_name='line_items')

    labels = sgqlc.types.Field(sgqlc.types.list_of('CreateShipmentShippingLabelInput'), graphql_name='labels')

    notify_customer_via_shiphero = sgqlc.types.Field(Boolean, graphql_name='notify_customer_via_shiphero')

    notify_customer_via_store = sgqlc.types.Field(Boolean, graphql_name='notify_customer_via_store')

    shipped_off_shiphero = sgqlc.types.Field(Boolean, graphql_name='shipped_off_shiphero')

    profile = sgqlc.types.Field(String, graphql_name='profile')



class CreateShipmentLineItemInput(sgqlc.types.Input):
    __schema__ = shiphero_schema
    __field_names__ = ('line_item_id', 'quantity')
    line_item_id = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='line_item_id')

    quantity = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='quantity')



class CreateShipmentShippingLabelInput(sgqlc.types.Input):
    __schema__ = shiphero_schema
    __field_names__ = ('carrier', 'shipping_name', 'shipping_method', 'cost', 'address', 'dimensions', 'label', 'line_item_ids', 'tracking_number')
    carrier = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='carrier')

    shipping_name = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='shipping_name')

    shipping_method = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='shipping_method')

    cost = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='cost')

    address = sgqlc.types.Field(sgqlc.types.non_null(AddressInput), graphql_name='address')

    dimensions = sgqlc.types.Field(sgqlc.types.non_null('DimensionsInput'), graphql_name='dimensions')

    label = sgqlc.types.Field(sgqlc.types.non_null(CreateLabelResourceInput), graphql_name='label')

    line_item_ids = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(String)), graphql_name='line_item_ids')

    tracking_number = sgqlc.types.Field(String, graphql_name='tracking_number')



class CreateShippingLabelInput(sgqlc.types.Input):
    __schema__ = shiphero_schema
    __field_names__ = ('customer_account_id', 'carrier', 'shipping_name', 'shipping_method', 'cost', 'address', 'dimensions', 'label', 'line_item_ids', 'tracking_number', 'shipment_id')
    customer_account_id = sgqlc.types.Field(String, graphql_name='customer_account_id')

    carrier = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='carrier')

    shipping_name = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='shipping_name')

    shipping_method = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='shipping_method')

    cost = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='cost')

    address = sgqlc.types.Field(sgqlc.types.non_null(AddressInput), graphql_name='address')

    dimensions = sgqlc.types.Field(sgqlc.types.non_null('DimensionsInput'), graphql_name='dimensions')

    label = sgqlc.types.Field(sgqlc.types.non_null(CreateLabelResourceInput), graphql_name='label')

    line_item_ids = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(String)), graphql_name='line_item_ids')

    tracking_number = sgqlc.types.Field(String, graphql_name='tracking_number')

    shipment_id = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='shipment_id')



class CreateShippingLinesInput(sgqlc.types.Input):
    __schema__ = shiphero_schema
    __field_names__ = ('title', 'price', 'carrier', 'method')
    title = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='title')

    price = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='price')

    carrier = sgqlc.types.Field(String, graphql_name='carrier')

    method = sgqlc.types.Field(String, graphql_name='method')



class CreateShippingPlanInput(sgqlc.types.Input):
    __schema__ = shiphero_schema
    __field_names__ = ('subtotal', 'shipping_price', 'total_price', 'warehouse_id', 'warehouse_note', 'vendor_po_number', 'line_items', 'packages', 'pallet')
    subtotal = sgqlc.types.Field(String, graphql_name='subtotal')

    shipping_price = sgqlc.types.Field(String, graphql_name='shipping_price')

    total_price = sgqlc.types.Field(String, graphql_name='total_price')

    warehouse_id = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='warehouse_id')

    warehouse_note = sgqlc.types.Field(String, graphql_name='warehouse_note')

    vendor_po_number = sgqlc.types.Field(String, graphql_name='vendor_po_number')

    line_items = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of('LineItemInput')), graphql_name='line_items')

    packages = sgqlc.types.Field(sgqlc.types.list_of('PackageInput'), graphql_name='packages')

    pallet = sgqlc.types.Field('PalletData', graphql_name='pallet')



class CreateVendorInput(sgqlc.types.Input):
    __schema__ = shiphero_schema
    __field_names__ = ('customer_account_id', 'name', 'email', 'account_number', 'address', 'currency', 'internal_note', 'default_po_note', 'logo', 'partner_vendor_id')
    customer_account_id = sgqlc.types.Field(String, graphql_name='customer_account_id')

    name = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='name')

    email = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='email')

    account_number = sgqlc.types.Field(String, graphql_name='account_number')

    address = sgqlc.types.Field(AddressInput, graphql_name='address')

    currency = sgqlc.types.Field(String, graphql_name='currency')

    internal_note = sgqlc.types.Field(String, graphql_name='internal_note')

    default_po_note = sgqlc.types.Field(String, graphql_name='default_po_note')

    logo = sgqlc.types.Field(String, graphql_name='logo')

    partner_vendor_id = sgqlc.types.Field(Int, graphql_name='partner_vendor_id')



class CreateWarehouseProductInput(sgqlc.types.Input):
    __schema__ = shiphero_schema
    __field_names__ = ('warehouse_id', 'on_hand', 'inventory_bin', 'inventory_overstock_bin', 'reserve_inventory', 'replenishment_level', 'reorder_level', 'reorder_amount', 'custom', 'warehouse', 'value', 'value_currency', 'price')
    warehouse_id = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='warehouse_id')

    on_hand = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='on_hand')

    inventory_bin = sgqlc.types.Field(String, graphql_name='inventory_bin')

    inventory_overstock_bin = sgqlc.types.Field(String, graphql_name='inventory_overstock_bin')

    reserve_inventory = sgqlc.types.Field(Int, graphql_name='reserve_inventory')

    replenishment_level = sgqlc.types.Field(Int, graphql_name='replenishment_level')

    reorder_level = sgqlc.types.Field(Int, graphql_name='reorder_level')

    reorder_amount = sgqlc.types.Field(Int, graphql_name='reorder_amount')

    custom = sgqlc.types.Field(Boolean, graphql_name='custom')

    warehouse = sgqlc.types.Field(String, graphql_name='warehouse')

    value = sgqlc.types.Field(String, graphql_name='value')

    value_currency = sgqlc.types.Field(String, graphql_name='value_currency')

    price = sgqlc.types.Field(String, graphql_name='price')



class CreateWebhookInput(sgqlc.types.Input):
    __schema__ = shiphero_schema
    __field_names__ = ('customer_account_id', 'name', 'url', 'shop_name')
    customer_account_id = sgqlc.types.Field(String, graphql_name='customer_account_id')

    name = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='name')

    url = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='url')

    shop_name = sgqlc.types.Field(String, graphql_name='shop_name')



class DeleteBillInput(sgqlc.types.Input):
    __schema__ = shiphero_schema
    __field_names__ = ('customer_account_id', 'id')
    customer_account_id = sgqlc.types.Field(String, graphql_name='customer_account_id')

    id = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='id')



class DeleteLotInput(sgqlc.types.Input):
    __schema__ = shiphero_schema
    __field_names__ = ('lot_id',)
    lot_id = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='lot_id')



class DeleteProductInput(sgqlc.types.Input):
    __schema__ = shiphero_schema
    __field_names__ = ('customer_account_id', 'sku')
    customer_account_id = sgqlc.types.Field(String, graphql_name='customer_account_id')

    sku = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='sku')



class DeleteVendorInput(sgqlc.types.Input):
    __schema__ = shiphero_schema
    __field_names__ = ('customer_account_id', 'vendor_id')
    customer_account_id = sgqlc.types.Field(String, graphql_name='customer_account_id')

    vendor_id = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='vendor_id')



class DeleteWarehouseProductInput(sgqlc.types.Input):
    __schema__ = shiphero_schema
    __field_names__ = ('customer_account_id', 'sku', 'warehouse_id')
    customer_account_id = sgqlc.types.Field(String, graphql_name='customer_account_id')

    sku = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='sku')

    warehouse_id = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='warehouse_id')



class DeleteWebhookInput(sgqlc.types.Input):
    __schema__ = shiphero_schema
    __field_names__ = ('customer_account_id', 'name', 'shop_name')
    customer_account_id = sgqlc.types.Field(String, graphql_name='customer_account_id')

    name = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='name')

    shop_name = sgqlc.types.Field(String, graphql_name='shop_name')



class DimensionsInput(sgqlc.types.Input):
    __schema__ = shiphero_schema
    __field_names__ = ('weight', 'height', 'width', 'length')
    weight = sgqlc.types.Field(String, graphql_name='weight')

    height = sgqlc.types.Field(String, graphql_name='height')

    width = sgqlc.types.Field(String, graphql_name='width')

    length = sgqlc.types.Field(String, graphql_name='length')



class HoldsInput(sgqlc.types.Input):
    __schema__ = shiphero_schema
    __field_names__ = ('payment_hold', 'operator_hold', 'fraud_hold', 'address_hold', 'client_hold')
    payment_hold = sgqlc.types.Field(Boolean, graphql_name='payment_hold')

    operator_hold = sgqlc.types.Field(Boolean, graphql_name='operator_hold')

    fraud_hold = sgqlc.types.Field(Boolean, graphql_name='fraud_hold')

    address_hold = sgqlc.types.Field(Boolean, graphql_name='address_hold')

    client_hold = sgqlc.types.Field(Boolean, graphql_name='client_hold')



class InventoryAbortSnapshotInput(sgqlc.types.Input):
    __schema__ = shiphero_schema
    __field_names__ = ('snapshot_id', 'reason')
    snapshot_id = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='snapshot_id')

    reason = sgqlc.types.Field(String, graphql_name='reason')



class InventoryGenerateSnapshotInput(sgqlc.types.Input):
    __schema__ = shiphero_schema
    __field_names__ = ('customer_account_id', 'warehouse_id', 'notification_email', 'post_url', 'post_url_pre_check', 'new_format')
    customer_account_id = sgqlc.types.Field(String, graphql_name='customer_account_id')

    warehouse_id = sgqlc.types.Field(String, graphql_name='warehouse_id')

    notification_email = sgqlc.types.Field(String, graphql_name='notification_email')

    post_url = sgqlc.types.Field(String, graphql_name='post_url')

    post_url_pre_check = sgqlc.types.Field(Boolean, graphql_name='post_url_pre_check')

    new_format = sgqlc.types.Field(Boolean, graphql_name='new_format')



class InventorySyncInput(sgqlc.types.Input):
    __schema__ = shiphero_schema
    __field_names__ = ('customer_account_id', 'url', 'warehouse_id')
    customer_account_id = sgqlc.types.Field(String, graphql_name='customer_account_id')

    url = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='url')

    warehouse_id = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='warehouse_id')



class LineItemInput(sgqlc.types.Input):
    __schema__ = shiphero_schema
    __field_names__ = ('product_name', 'sku', 'quantity')
    product_name = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='product_name')

    sku = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='sku')

    quantity = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='quantity')



class OrderNoteAttributeInput(sgqlc.types.Input):
    __schema__ = shiphero_schema
    __field_names__ = ('name', 'value')
    name = sgqlc.types.Field(String, graphql_name='name')

    value = sgqlc.types.Field(String, graphql_name='value')



class PackageInput(sgqlc.types.Input):
    __schema__ = shiphero_schema
    __field_names__ = ('line_items',)
    line_items = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of('PackageLineItemInput')), graphql_name='line_items')



class PackageLineItemInput(sgqlc.types.Input):
    __schema__ = shiphero_schema
    __field_names__ = ('sku', 'quantity')
    sku = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='sku')

    quantity = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='quantity')



class PalletData(sgqlc.types.Input):
    __schema__ = shiphero_schema
    __field_names__ = ('quantity', 'kind', 'page_size', 'floor_loaded')
    quantity = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='quantity')

    kind = sgqlc.types.Field(String, graphql_name='kind')

    page_size = sgqlc.types.Field(String, graphql_name='page_size')

    floor_loaded = sgqlc.types.Field(Boolean, graphql_name='floor_loaded')



class RecalculateBillInput(sgqlc.types.Input):
    __schema__ = shiphero_schema
    __field_names__ = ('customer_account_id', 'id')
    customer_account_id = sgqlc.types.Field(String, graphql_name='customer_account_id')

    id = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='id')



class RemoveKitComponentInput(sgqlc.types.Input):
    __schema__ = shiphero_schema
    __field_names__ = ('customer_account_id', 'sku')
    customer_account_id = sgqlc.types.Field(String, graphql_name='customer_account_id')

    sku = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='sku')



class RemoveKitComponentsInput(sgqlc.types.Input):
    __schema__ = shiphero_schema
    __field_names__ = ('customer_account_id', 'sku', 'components')
    customer_account_id = sgqlc.types.Field(String, graphql_name='customer_account_id')

    sku = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='sku')

    components = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(RemoveKitComponentInput)), graphql_name='components')



class RemoveLineItemsInput(sgqlc.types.Input):
    __schema__ = shiphero_schema
    __field_names__ = ('customer_account_id', 'order_id', 'line_item_ids')
    customer_account_id = sgqlc.types.Field(String, graphql_name='customer_account_id')

    order_id = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='order_id')

    line_item_ids = sgqlc.types.Field(sgqlc.types.list_of(String), graphql_name='line_item_ids')



class RemoveProductFromVendorInput(sgqlc.types.Input):
    __schema__ = shiphero_schema
    __field_names__ = ('customer_account_id', 'vendor_id', 'sku')
    customer_account_id = sgqlc.types.Field(String, graphql_name='customer_account_id')

    vendor_id = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='vendor_id')

    sku = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='sku')



class ReplaceInventoryInput(sgqlc.types.Input):
    __schema__ = shiphero_schema
    __field_names__ = ('customer_account_id', 'sku', 'warehouse_id', 'quantity', 'reason', 'location_id', 'includes_non_sellable')
    customer_account_id = sgqlc.types.Field(String, graphql_name='customer_account_id')

    sku = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='sku')

    warehouse_id = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='warehouse_id')

    quantity = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='quantity')

    reason = sgqlc.types.Field(String, graphql_name='reason')

    location_id = sgqlc.types.Field(String, graphql_name='location_id')

    includes_non_sellable = sgqlc.types.Field(Boolean, graphql_name='includes_non_sellable')



class SetPurchaseOrderFulfillmentStatusInput(sgqlc.types.Input):
    __schema__ = shiphero_schema
    __field_names__ = ('customer_account_id', 'po_id', 'status')
    customer_account_id = sgqlc.types.Field(String, graphql_name='customer_account_id')

    po_id = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='po_id')

    status = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='status')



class SubmitBillInput(sgqlc.types.Input):
    __schema__ = shiphero_schema
    __field_names__ = ('customer_account_id', 'id')
    customer_account_id = sgqlc.types.Field(String, graphql_name='customer_account_id')

    id = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='id')



class UpdateBillInput(sgqlc.types.Input):
    __schema__ = shiphero_schema
    __field_names__ = ('customer_account_id', 'id', 'status')
    customer_account_id = sgqlc.types.Field(String, graphql_name='customer_account_id')

    id = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='id')

    status = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='status')



class UpdateInventoryInput(sgqlc.types.Input):
    __schema__ = shiphero_schema
    __field_names__ = ('customer_account_id', 'sku', 'warehouse_id', 'quantity', 'reason', 'location_id')
    customer_account_id = sgqlc.types.Field(String, graphql_name='customer_account_id')

    sku = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='sku')

    warehouse_id = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='warehouse_id')

    quantity = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='quantity')

    reason = sgqlc.types.Field(String, graphql_name='reason')

    location_id = sgqlc.types.Field(String, graphql_name='location_id')



class UpdateLineItemInput(sgqlc.types.Input):
    __schema__ = shiphero_schema
    __field_names__ = ('id', 'partner_line_item_id', 'quantity', 'price', 'product_name', 'option_title', 'fulfillment_status', 'quantity_pending_fulfillment', 'custom_options', 'custom_barcode', 'eligible_for_return', 'customs_value', 'warehouse_id', 'barcode')
    id = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='id')

    partner_line_item_id = sgqlc.types.Field(String, graphql_name='partner_line_item_id')

    quantity = sgqlc.types.Field(Int, graphql_name='quantity')

    price = sgqlc.types.Field(String, graphql_name='price')

    product_name = sgqlc.types.Field(String, graphql_name='product_name')

    option_title = sgqlc.types.Field(String, graphql_name='option_title')

    fulfillment_status = sgqlc.types.Field(String, graphql_name='fulfillment_status')

    quantity_pending_fulfillment = sgqlc.types.Field(Int, graphql_name='quantity_pending_fulfillment')

    custom_options = sgqlc.types.Field(GenericScalar, graphql_name='custom_options')

    custom_barcode = sgqlc.types.Field(String, graphql_name='custom_barcode')

    eligible_for_return = sgqlc.types.Field(Boolean, graphql_name='eligible_for_return')

    customs_value = sgqlc.types.Field(String, graphql_name='customs_value')

    warehouse_id = sgqlc.types.Field(String, graphql_name='warehouse_id')

    barcode = sgqlc.types.Field(String, graphql_name='barcode')



class UpdateLineItemsInput(sgqlc.types.Input):
    __schema__ = shiphero_schema
    __field_names__ = ('customer_account_id', 'order_id', 'line_items')
    customer_account_id = sgqlc.types.Field(String, graphql_name='customer_account_id')

    order_id = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='order_id')

    line_items = sgqlc.types.Field(sgqlc.types.list_of(UpdateLineItemInput), graphql_name='line_items')



class UpdateLocationInput(sgqlc.types.Input):
    __schema__ = shiphero_schema
    __field_names__ = ('location_id', 'zone', 'location_type_id', 'pickable', 'sellable', 'is_cart', 'pick_priority', 'dimensions', 'temperature')
    location_id = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='location_id')

    zone = sgqlc.types.Field(String, graphql_name='zone')

    location_type_id = sgqlc.types.Field(String, graphql_name='location_type_id')

    pickable = sgqlc.types.Field(Boolean, graphql_name='pickable')

    sellable = sgqlc.types.Field(Boolean, graphql_name='sellable')

    is_cart = sgqlc.types.Field(Boolean, graphql_name='is_cart')

    pick_priority = sgqlc.types.Field(Int, graphql_name='pick_priority')

    dimensions = sgqlc.types.Field(DimensionsInput, graphql_name='dimensions')

    temperature = sgqlc.types.Field(String, graphql_name='temperature')



class UpdateLotInput(sgqlc.types.Input):
    __schema__ = shiphero_schema
    __field_names__ = ('lot_id', 'name', 'sku', 'expires_at', 'is_active')
    lot_id = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='lot_id')

    name = sgqlc.types.Field(String, graphql_name='name')

    sku = sgqlc.types.Field(String, graphql_name='sku')

    expires_at = sgqlc.types.Field(ISODateTime, graphql_name='expires_at')

    is_active = sgqlc.types.Field(Boolean, graphql_name='is_active')



class UpdateLotsInput(sgqlc.types.Input):
    __schema__ = shiphero_schema
    __field_names__ = ('lots_ids', 'is_active')
    lots_ids = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(String)), graphql_name='lots_ids')

    is_active = sgqlc.types.Field(Boolean, graphql_name='is_active')



class UpdateOrderFulfillmentStatusInput(sgqlc.types.Input):
    __schema__ = shiphero_schema
    __field_names__ = ('customer_account_id', 'order_id', 'fulfillment_status', 'remove_inventory', 'reason', 'void_on_platform')
    customer_account_id = sgqlc.types.Field(String, graphql_name='customer_account_id')

    order_id = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='order_id')

    fulfillment_status = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='fulfillment_status')

    remove_inventory = sgqlc.types.Field(Boolean, graphql_name='remove_inventory')

    reason = sgqlc.types.Field(String, graphql_name='reason')

    void_on_platform = sgqlc.types.Field(Boolean, graphql_name='void_on_platform')



class UpdateOrderHoldsInput(sgqlc.types.Input):
    __schema__ = shiphero_schema
    __field_names__ = ('customer_account_id', 'order_id', 'payment_hold', 'operator_hold', 'fraud_hold', 'address_hold', 'client_hold')
    customer_account_id = sgqlc.types.Field(String, graphql_name='customer_account_id')

    order_id = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='order_id')

    payment_hold = sgqlc.types.Field(Boolean, graphql_name='payment_hold')

    operator_hold = sgqlc.types.Field(Boolean, graphql_name='operator_hold')

    fraud_hold = sgqlc.types.Field(Boolean, graphql_name='fraud_hold')

    address_hold = sgqlc.types.Field(Boolean, graphql_name='address_hold')

    client_hold = sgqlc.types.Field(Boolean, graphql_name='client_hold')



class UpdateOrderInput(sgqlc.types.Input):
    __schema__ = shiphero_schema
    __field_names__ = ('customer_account_id', 'order_id', 'order_number', 'partner_order_id', 'fulfillment_status', 'order_date', 'total_tax', 'subtotal', 'total_discounts', 'total_price', 'box_name', 'ready_to_ship', 'required_ship_date', 'allocation_priority', 'shipping_lines', 'shipping_address', 'billing_address', 'profile', 'packing_note', 'note_attributes', 'tags', 'gift_note', 'gift_invoice', 'require_signature', 'adult_signature_required', 'alcohol', 'insurance', 'allow_partial', 'allow_split', 'priority_flag', 'hold_until_date', 'incoterms', 'tax_id', 'tax_type', 'history_entry', 'ignore_address_validation_errors', 'skip_address_validation', 'custom_invoice_url', 'auto_print_return_label', 'dry_ice_weight_in_lbs', 'ftr_exemption', 'address_is_business')
    customer_account_id = sgqlc.types.Field(String, graphql_name='customer_account_id')

    order_id = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='order_id')

    order_number = sgqlc.types.Field(String, graphql_name='order_number')

    partner_order_id = sgqlc.types.Field(String, graphql_name='partner_order_id')

    fulfillment_status = sgqlc.types.Field(String, graphql_name='fulfillment_status')

    order_date = sgqlc.types.Field(ISODateTime, graphql_name='order_date')

    total_tax = sgqlc.types.Field(String, graphql_name='total_tax')

    subtotal = sgqlc.types.Field(String, graphql_name='subtotal')

    total_discounts = sgqlc.types.Field(String, graphql_name='total_discounts')

    total_price = sgqlc.types.Field(String, graphql_name='total_price')

    box_name = sgqlc.types.Field(String, graphql_name='box_name')

    ready_to_ship = sgqlc.types.Field(Boolean, graphql_name='ready_to_ship')

    required_ship_date = sgqlc.types.Field(ISODateTime, graphql_name='required_ship_date')

    allocation_priority = sgqlc.types.Field(Int, graphql_name='allocation_priority')

    shipping_lines = sgqlc.types.Field(CreateShippingLinesInput, graphql_name='shipping_lines')

    shipping_address = sgqlc.types.Field(CreateOrderAddressInput, graphql_name='shipping_address')

    billing_address = sgqlc.types.Field(CreateOrderAddressInput, graphql_name='billing_address')

    profile = sgqlc.types.Field(String, graphql_name='profile')

    packing_note = sgqlc.types.Field(String, graphql_name='packing_note')

    note_attributes = sgqlc.types.Field(sgqlc.types.list_of(OrderNoteAttributeInput), graphql_name='note_attributes')

    tags = sgqlc.types.Field(sgqlc.types.list_of(String), graphql_name='tags')

    gift_note = sgqlc.types.Field(String, graphql_name='gift_note')

    gift_invoice = sgqlc.types.Field(Boolean, graphql_name='gift_invoice')

    require_signature = sgqlc.types.Field(Boolean, graphql_name='require_signature')

    adult_signature_required = sgqlc.types.Field(Boolean, graphql_name='adult_signature_required')

    alcohol = sgqlc.types.Field(Boolean, graphql_name='alcohol')

    insurance = sgqlc.types.Field(Boolean, graphql_name='insurance')

    allow_partial = sgqlc.types.Field(Boolean, graphql_name='allow_partial')

    allow_split = sgqlc.types.Field(Boolean, graphql_name='allow_split')

    priority_flag = sgqlc.types.Field(Boolean, graphql_name='priority_flag')

    hold_until_date = sgqlc.types.Field(ISODateTime, graphql_name='hold_until_date')

    incoterms = sgqlc.types.Field(String, graphql_name='incoterms')

    tax_id = sgqlc.types.Field(String, graphql_name='tax_id')

    tax_type = sgqlc.types.Field(String, graphql_name='tax_type')

    history_entry = sgqlc.types.Field('UserNoteInput', graphql_name='history_entry')

    ignore_address_validation_errors = sgqlc.types.Field(Boolean, graphql_name='ignore_address_validation_errors')

    skip_address_validation = sgqlc.types.Field(Boolean, graphql_name='skip_address_validation')

    custom_invoice_url = sgqlc.types.Field(String, graphql_name='custom_invoice_url')

    auto_print_return_label = sgqlc.types.Field(Boolean, graphql_name='auto_print_return_label')

    dry_ice_weight_in_lbs = sgqlc.types.Field(String, graphql_name='dry_ice_weight_in_lbs')

    ftr_exemption = sgqlc.types.Field(Decimal, graphql_name='ftr_exemption')

    address_is_business = sgqlc.types.Field(Boolean, graphql_name='address_is_business')



class UpdateOrderInputBase(sgqlc.types.Input):
    __schema__ = shiphero_schema
    __field_names__ = ('customer_account_id', 'order_id')
    customer_account_id = sgqlc.types.Field(String, graphql_name='customer_account_id')

    order_id = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='order_id')



class UpdateProductImageInput(sgqlc.types.Input):
    __schema__ = shiphero_schema
    __field_names__ = ('src', 'position')
    src = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='src')

    position = sgqlc.types.Field(Int, graphql_name='position')



class UpdateProductInput(sgqlc.types.Input):
    __schema__ = shiphero_schema
    __field_names__ = ('customer_account_id', 'sku', 'name', 'dimensions', 'tariff_code', 'product_note', 'country_of_manufacture', 'needs_serial_number', 'dropship', 'barcode', 'customs_description', 'tags', 'vendors', 'final_sale', 'virtual', 'needs_lot_tracking', 'images', 'packer_note')
    customer_account_id = sgqlc.types.Field(String, graphql_name='customer_account_id')

    sku = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='sku')

    name = sgqlc.types.Field(String, graphql_name='name')

    dimensions = sgqlc.types.Field(DimensionsInput, graphql_name='dimensions')

    tariff_code = sgqlc.types.Field(String, graphql_name='tariff_code')

    product_note = sgqlc.types.Field(String, graphql_name='product_note')

    country_of_manufacture = sgqlc.types.Field(String, graphql_name='country_of_manufacture')

    needs_serial_number = sgqlc.types.Field(Boolean, graphql_name='needs_serial_number')

    dropship = sgqlc.types.Field(Boolean, graphql_name='dropship')

    barcode = sgqlc.types.Field(String, graphql_name='barcode')

    customs_description = sgqlc.types.Field(String, graphql_name='customs_description')

    tags = sgqlc.types.Field(sgqlc.types.list_of(String), graphql_name='tags')

    vendors = sgqlc.types.Field(sgqlc.types.list_of('UpdateProductVendorInput'), graphql_name='vendors')

    final_sale = sgqlc.types.Field(Boolean, graphql_name='final_sale')

    virtual = sgqlc.types.Field(Boolean, graphql_name='virtual')

    needs_lot_tracking = sgqlc.types.Field(Boolean, graphql_name='needs_lot_tracking')

    images = sgqlc.types.Field(sgqlc.types.list_of(UpdateProductImageInput), graphql_name='images')

    packer_note = sgqlc.types.Field(String, graphql_name='packer_note')



class UpdateProductVendorInput(sgqlc.types.Input):
    __schema__ = shiphero_schema
    __field_names__ = ('customer_account_id', 'vendor_id', 'vendor_sku', 'price')
    customer_account_id = sgqlc.types.Field(String, graphql_name='customer_account_id')

    vendor_id = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='vendor_id')

    vendor_sku = sgqlc.types.Field(String, graphql_name='vendor_sku')

    price = sgqlc.types.Field(String, graphql_name='price')



class UpdatePurchaseOrderInput(sgqlc.types.Input):
    __schema__ = shiphero_schema
    __field_names__ = ('customer_account_id', 'po_id', 'packing_note', 'po_note', 'description', 'partner_order_number', 'discount', 'tax', 'line_items', 'shipping_method', 'shipping_carrier', 'shipping_name', 'shipping_price', 'tracking_number', 'pdf', 'payment_method', 'payment_due_by', 'payment_note', 'po_date', 'clear_po_date')
    customer_account_id = sgqlc.types.Field(String, graphql_name='customer_account_id')

    po_id = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='po_id')

    packing_note = sgqlc.types.Field(String, graphql_name='packing_note')

    po_note = sgqlc.types.Field(String, graphql_name='po_note')

    description = sgqlc.types.Field(String, graphql_name='description')

    partner_order_number = sgqlc.types.Field(String, graphql_name='partner_order_number')

    discount = sgqlc.types.Field(String, graphql_name='discount')

    tax = sgqlc.types.Field(String, graphql_name='tax')

    line_items = sgqlc.types.Field(sgqlc.types.list_of('UpdatePurchaseOrderLineItemInput'), graphql_name='line_items')

    shipping_method = sgqlc.types.Field(String, graphql_name='shipping_method')

    shipping_carrier = sgqlc.types.Field(String, graphql_name='shipping_carrier')

    shipping_name = sgqlc.types.Field(String, graphql_name='shipping_name')

    shipping_price = sgqlc.types.Field(String, graphql_name='shipping_price')

    tracking_number = sgqlc.types.Field(String, graphql_name='tracking_number')

    pdf = sgqlc.types.Field(String, graphql_name='pdf')

    payment_method = sgqlc.types.Field(String, graphql_name='payment_method')

    payment_due_by = sgqlc.types.Field(String, graphql_name='payment_due_by')

    payment_note = sgqlc.types.Field(String, graphql_name='payment_note')

    po_date = sgqlc.types.Field(ISODateTime, graphql_name='po_date')

    clear_po_date = sgqlc.types.Field(Boolean, graphql_name='clear_po_date')



class UpdatePurchaseOrderLineItemInput(sgqlc.types.Input):
    __schema__ = shiphero_schema
    __field_names__ = ('sku', 'quantity', 'quantity_received', 'quantity_rejected', 'sell_ahead', 'price', 'note')
    sku = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='sku')

    quantity = sgqlc.types.Field(Int, graphql_name='quantity')

    quantity_received = sgqlc.types.Field(Int, graphql_name='quantity_received')

    quantity_rejected = sgqlc.types.Field(Int, graphql_name='quantity_rejected')

    sell_ahead = sgqlc.types.Field(Int, graphql_name='sell_ahead')

    price = sgqlc.types.Field(String, graphql_name='price')

    note = sgqlc.types.Field(String, graphql_name='note')



class UpdateReturnStatusInput(sgqlc.types.Input):
    __schema__ = shiphero_schema
    __field_names__ = ('return_id', 'status')
    return_id = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='return_id')

    status = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='status')



class UpdateTagsInput(sgqlc.types.Input):
    __schema__ = shiphero_schema
    __field_names__ = ('customer_account_id', 'order_id', 'tags')
    customer_account_id = sgqlc.types.Field(String, graphql_name='customer_account_id')

    order_id = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='order_id')

    tags = sgqlc.types.Field(sgqlc.types.list_of(String), graphql_name='tags')



class UpdateWarehouseProductInput(sgqlc.types.Input):
    __schema__ = shiphero_schema
    __field_names__ = ('customer_account_id', 'sku', 'warehouse_id', 'on_hand', 'price', 'value', 'value_currency', 'inventory_bin', 'inventory_overstock_bin', 'reserve_inventory', 'replenishment_level', 'reorder_amount', 'reorder_level', 'customs_value', 'active')
    customer_account_id = sgqlc.types.Field(String, graphql_name='customer_account_id')

    sku = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='sku')

    warehouse_id = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='warehouse_id')

    on_hand = sgqlc.types.Field(Int, graphql_name='on_hand')

    price = sgqlc.types.Field(String, graphql_name='price')

    value = sgqlc.types.Field(String, graphql_name='value')

    value_currency = sgqlc.types.Field(String, graphql_name='value_currency')

    inventory_bin = sgqlc.types.Field(String, graphql_name='inventory_bin')

    inventory_overstock_bin = sgqlc.types.Field(String, graphql_name='inventory_overstock_bin')

    reserve_inventory = sgqlc.types.Field(Int, graphql_name='reserve_inventory')

    replenishment_level = sgqlc.types.Field(Int, graphql_name='replenishment_level')

    reorder_amount = sgqlc.types.Field(Int, graphql_name='reorder_amount')

    reorder_level = sgqlc.types.Field(Int, graphql_name='reorder_level')

    customs_value = sgqlc.types.Field(String, graphql_name='customs_value')

    active = sgqlc.types.Field(Boolean, graphql_name='active')



class UserNoteInput(sgqlc.types.Input):
    __schema__ = shiphero_schema
    __field_names__ = ('source', 'message')
    source = sgqlc.types.Field(String, graphql_name='source')

    message = sgqlc.types.Field(String, graphql_name='message')




########################################################################
# Output Objects and Interfaces
########################################################################
class AbortInventorySyncOutput(sgqlc.types.Type):
    __schema__ = shiphero_schema
    __field_names__ = ('request_id', 'complexity', 'sync')
    request_id = sgqlc.types.Field(String, graphql_name='request_id')

    complexity = sgqlc.types.Field(Int, graphql_name='complexity')

    sync = sgqlc.types.Field('InventorySyncStatus', graphql_name='sync')



class Account(sgqlc.types.Type):
    __schema__ = shiphero_schema
    __field_names__ = ('id', 'legacy_id', 'email', 'username', 'status', 'dynamic_slotting', 'is_multi_warehouse', 'is_3pl', 'cycle_count_enabled', 'ship_backorders', 'customers', 'warehouses')
    id = sgqlc.types.Field(String, graphql_name='id')

    legacy_id = sgqlc.types.Field(Int, graphql_name='legacy_id')

    email = sgqlc.types.Field(String, graphql_name='email')

    username = sgqlc.types.Field(String, graphql_name='username')

    status = sgqlc.types.Field(String, graphql_name='status')

    dynamic_slotting = sgqlc.types.Field(Boolean, graphql_name='dynamic_slotting')

    is_multi_warehouse = sgqlc.types.Field(Boolean, graphql_name='is_multi_warehouse')

    is_3pl = sgqlc.types.Field(Boolean, graphql_name='is_3pl')

    cycle_count_enabled = sgqlc.types.Field(Boolean, graphql_name='cycle_count_enabled')

    ship_backorders = sgqlc.types.Field(Boolean, graphql_name='ship_backorders')

    customers = sgqlc.types.Field('AccountConnection', graphql_name='customers', args=sgqlc.types.ArgDict((
        ('warehouse_id', sgqlc.types.Arg(String, graphql_name='warehouse_id', default=None)),
        ('sort', sgqlc.types.Arg(String, graphql_name='sort', default=None)),
        ('before', sgqlc.types.Arg(String, graphql_name='before', default=None)),
        ('after', sgqlc.types.Arg(String, graphql_name='after', default=None)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
))
    )
    '''Arguments:

    * `warehouse_id` (`String`)
    * `sort` (`String`)
    * `before` (`String`)
    * `after` (`String`)
    * `first` (`Int`)
    * `last` (`Int`)
    '''

    warehouses = sgqlc.types.Field(sgqlc.types.list_of('Warehouse'), graphql_name='warehouses')



class AccountConnection(sgqlc.types.relay.Connection):
    __schema__ = shiphero_schema
    __field_names__ = ('page_info', 'edges')
    page_info = sgqlc.types.Field(sgqlc.types.non_null('PageInfo'), graphql_name='pageInfo')

    edges = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of('AccountEdge')), graphql_name='edges')



class AccountEdge(sgqlc.types.Type):
    __schema__ = shiphero_schema
    __field_names__ = ('node', 'cursor')
    node = sgqlc.types.Field(Account, graphql_name='node')

    cursor = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='cursor')



class AccountQueryResult(sgqlc.types.Type):
    __schema__ = shiphero_schema
    __field_names__ = ('request_id', 'complexity', 'data')
    request_id = sgqlc.types.Field(String, graphql_name='request_id')

    complexity = sgqlc.types.Field(Int, graphql_name='complexity')

    data = sgqlc.types.Field(Account, graphql_name='data')



class AddPurchaseOrderAttachmentOutput(sgqlc.types.Type):
    __schema__ = shiphero_schema
    __field_names__ = ('request_id', 'complexity', 'attachment')
    request_id = sgqlc.types.Field(String, graphql_name='request_id')

    complexity = sgqlc.types.Field(Int, graphql_name='complexity')

    attachment = sgqlc.types.Field('PurchaseOrderAttachment', graphql_name='attachment')



class Address(sgqlc.types.Type):
    __schema__ = shiphero_schema
    __field_names__ = ('name', 'address1', 'address2', 'city', 'state', 'country', 'zip', 'phone')
    name = sgqlc.types.Field(String, graphql_name='name')

    address1 = sgqlc.types.Field(String, graphql_name='address1')

    address2 = sgqlc.types.Field(String, graphql_name='address2')

    city = sgqlc.types.Field(String, graphql_name='city')

    state = sgqlc.types.Field(String, graphql_name='state')

    country = sgqlc.types.Field(String, graphql_name='country')

    zip = sgqlc.types.Field(String, graphql_name='zip')

    phone = sgqlc.types.Field(String, graphql_name='phone')



class AssignLotToLocationOutput(sgqlc.types.Type):
    __schema__ = shiphero_schema
    __field_names__ = ('request_id', 'complexity', 'warehouse_product')
    request_id = sgqlc.types.Field(String, graphql_name='request_id')

    complexity = sgqlc.types.Field(Int, graphql_name='complexity')

    warehouse_product = sgqlc.types.Field('WarehouseProduct', graphql_name='warehouse_product')



class Authorization(sgqlc.types.Type):
    __schema__ = shiphero_schema
    __field_names__ = ('transaction_id', 'authorized_amount', 'postauthed_amount', 'refunded_amount', 'card_type', 'date')
    transaction_id = sgqlc.types.Field(String, graphql_name='transaction_id')

    authorized_amount = sgqlc.types.Field(String, graphql_name='authorized_amount')

    postauthed_amount = sgqlc.types.Field(String, graphql_name='postauthed_amount')

    refunded_amount = sgqlc.types.Field(String, graphql_name='refunded_amount')

    card_type = sgqlc.types.Field(String, graphql_name='card_type')

    date = sgqlc.types.Field(ISODateTime, graphql_name='date')



class Bill(sgqlc.types.Type):
    __schema__ = shiphero_schema
    __field_names__ = ('id', 'legacy_id', 'status', 'customer_name', 'profile_name', 'created_at', 'due_date', 'amount', 'totals', 'bill_exports', 'billing_period', 'billing_frequency')
    id = sgqlc.types.Field(String, graphql_name='id')

    legacy_id = sgqlc.types.Field(Int, graphql_name='legacy_id')

    status = sgqlc.types.Field(String, graphql_name='status')

    customer_name = sgqlc.types.Field(String, graphql_name='customer_name')

    profile_name = sgqlc.types.Field(String, graphql_name='profile_name')

    created_at = sgqlc.types.Field(ISODateTime, graphql_name='created_at')

    due_date = sgqlc.types.Field(ISODateTime, graphql_name='due_date')

    amount = sgqlc.types.Field(Money, graphql_name='amount')

    totals = sgqlc.types.Field('FeeCategoryTotalConnection', graphql_name='totals', args=sgqlc.types.ArgDict((
        ('sort', sgqlc.types.Arg(String, graphql_name='sort', default=None)),
        ('before', sgqlc.types.Arg(String, graphql_name='before', default=None)),
        ('after', sgqlc.types.Arg(String, graphql_name='after', default=None)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
))
    )
    '''Arguments:

    * `sort` (`String`)
    * `before` (`String`)
    * `after` (`String`)
    * `first` (`Int`)
    * `last` (`Int`)
    '''

    bill_exports = sgqlc.types.Field('BillExportsConnection', graphql_name='bill_exports', args=sgqlc.types.ArgDict((
        ('sort', sgqlc.types.Arg(String, graphql_name='sort', default=None)),
        ('before', sgqlc.types.Arg(String, graphql_name='before', default=None)),
        ('after', sgqlc.types.Arg(String, graphql_name='after', default=None)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
))
    )
    '''Arguments:

    * `sort` (`String`)
    * `before` (`String`)
    * `after` (`String`)
    * `first` (`Int`)
    * `last` (`Int`)
    '''

    billing_period = sgqlc.types.Field('BillingPeriod', graphql_name='billing_period')

    billing_frequency = sgqlc.types.Field(String, graphql_name='billing_frequency')



class BillConnection(sgqlc.types.relay.Connection):
    __schema__ = shiphero_schema
    __field_names__ = ('page_info', 'edges')
    page_info = sgqlc.types.Field(sgqlc.types.non_null('PageInfo'), graphql_name='pageInfo')

    edges = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of('BillEdge')), graphql_name='edges')



class BillEdge(sgqlc.types.Type):
    __schema__ = shiphero_schema
    __field_names__ = ('node', 'cursor')
    node = sgqlc.types.Field(Bill, graphql_name='node')

    cursor = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='cursor')



class BillExports(sgqlc.types.Type):
    __schema__ = shiphero_schema
    __field_names__ = ('id', 'legacy_id', 'status', 'file_url')
    id = sgqlc.types.Field(String, graphql_name='id')

    legacy_id = sgqlc.types.Field(Int, graphql_name='legacy_id')

    status = sgqlc.types.Field(String, graphql_name='status')

    file_url = sgqlc.types.Field(String, graphql_name='file_url')



class BillExportsConnection(sgqlc.types.relay.Connection):
    __schema__ = shiphero_schema
    __field_names__ = ('page_info', 'edges')
    page_info = sgqlc.types.Field(sgqlc.types.non_null('PageInfo'), graphql_name='pageInfo')

    edges = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of('BillExportsEdge')), graphql_name='edges')



class BillExportsEdge(sgqlc.types.Type):
    __schema__ = shiphero_schema
    __field_names__ = ('node', 'cursor')
    node = sgqlc.types.Field(BillExports, graphql_name='node')

    cursor = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='cursor')



class BillQueryResult(sgqlc.types.Type):
    __schema__ = shiphero_schema
    __field_names__ = ('request_id', 'complexity', 'data')
    request_id = sgqlc.types.Field(String, graphql_name='request_id')

    complexity = sgqlc.types.Field(Int, graphql_name='complexity')

    data = sgqlc.types.Field(Bill, graphql_name='data')



class BillingPeriod(sgqlc.types.Type):
    __schema__ = shiphero_schema
    __field_names__ = ('start', 'end')
    start = sgqlc.types.Field(ISODateTime, graphql_name='start')

    end = sgqlc.types.Field(ISODateTime, graphql_name='end')



class BillsQueryResult(sgqlc.types.Type):
    __schema__ = shiphero_schema
    __field_names__ = ('request_id', 'complexity', 'data')
    request_id = sgqlc.types.Field(String, graphql_name='request_id')

    complexity = sgqlc.types.Field(Int, graphql_name='complexity')

    data = sgqlc.types.Field(BillConnection, graphql_name='data', args=sgqlc.types.ArgDict((
        ('sort', sgqlc.types.Arg(String, graphql_name='sort', default=None)),
        ('before', sgqlc.types.Arg(String, graphql_name='before', default=None)),
        ('after', sgqlc.types.Arg(String, graphql_name='after', default=None)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
))
    )
    '''Arguments:

    * `sort` (`String`)
    * `before` (`String`)
    * `after` (`String`)
    * `first` (`Int`)
    * `last` (`Int`)
    '''



class CancelPurchaseOrderOutput(sgqlc.types.Type):
    __schema__ = shiphero_schema
    __field_names__ = ('request_id', 'complexity', 'purchase_order')
    request_id = sgqlc.types.Field(String, graphql_name='request_id')

    complexity = sgqlc.types.Field(Int, graphql_name='complexity')

    purchase_order = sgqlc.types.Field('PurchaseOrder', graphql_name='purchase_order')



class ClosePurchaseOrderOutput(sgqlc.types.Type):
    __schema__ = shiphero_schema
    __field_names__ = ('request_id', 'complexity', 'purchase_order')
    request_id = sgqlc.types.Field(String, graphql_name='request_id')

    complexity = sgqlc.types.Field(Int, graphql_name='complexity')

    purchase_order = sgqlc.types.Field('PurchaseOrder', graphql_name='purchase_order')



class CreateBillOutput(sgqlc.types.Type):
    __schema__ = shiphero_schema
    __field_names__ = ('request_id', 'complexity', 'bill')
    request_id = sgqlc.types.Field(String, graphql_name='request_id')

    complexity = sgqlc.types.Field(Int, graphql_name='complexity')

    bill = sgqlc.types.Field(Bill, graphql_name='bill')



class CreateLotOutput(sgqlc.types.Type):
    __schema__ = shiphero_schema
    __field_names__ = ('request_id', 'complexity', 'lot')
    request_id = sgqlc.types.Field(String, graphql_name='request_id')

    complexity = sgqlc.types.Field(Int, graphql_name='complexity')

    lot = sgqlc.types.Field('Lot', graphql_name='lot')



class CreateProductOutput(sgqlc.types.Type):
    __schema__ = shiphero_schema
    __field_names__ = ('request_id', 'complexity', 'product')
    request_id = sgqlc.types.Field(String, graphql_name='request_id')

    complexity = sgqlc.types.Field(Int, graphql_name='complexity')

    product = sgqlc.types.Field('Product', graphql_name='product')



class CreatePurchaseOrderOutput(sgqlc.types.Type):
    __schema__ = shiphero_schema
    __field_names__ = ('request_id', 'complexity', 'purchase_order')
    request_id = sgqlc.types.Field(String, graphql_name='request_id')

    complexity = sgqlc.types.Field(Int, graphql_name='complexity')

    purchase_order = sgqlc.types.Field('PurchaseOrder', graphql_name='purchase_order')



class CreateReturnExchangeOutput(sgqlc.types.Type):
    __schema__ = shiphero_schema
    __field_names__ = ('request_id', 'complexity', 'return_exchange')
    request_id = sgqlc.types.Field(String, graphql_name='request_id')

    complexity = sgqlc.types.Field(Int, graphql_name='complexity')

    return_exchange = sgqlc.types.Field('ReturnExchange', graphql_name='return_exchange')



class CreateReturnOutput(sgqlc.types.Type):
    __schema__ = shiphero_schema
    __field_names__ = ('request_id', 'complexity', 'return_')
    request_id = sgqlc.types.Field(String, graphql_name='request_id')

    complexity = sgqlc.types.Field(Int, graphql_name='complexity')

    return_ = sgqlc.types.Field('Return', graphql_name='return')



class CreateShipmentOutput(sgqlc.types.Type):
    __schema__ = shiphero_schema
    __field_names__ = ('request_id', 'complexity', 'shipment')
    request_id = sgqlc.types.Field(String, graphql_name='request_id')

    complexity = sgqlc.types.Field(Int, graphql_name='complexity')

    shipment = sgqlc.types.Field('Shipment', graphql_name='shipment')



class CreateShippingLabelOutput(sgqlc.types.Type):
    __schema__ = shiphero_schema
    __field_names__ = ('request_id', 'complexity', 'shipping_label')
    request_id = sgqlc.types.Field(String, graphql_name='request_id')

    complexity = sgqlc.types.Field(Int, graphql_name='complexity')

    shipping_label = sgqlc.types.Field('ShippingLabel', graphql_name='shipping_label')



class CreateShippingPlanOutput(sgqlc.types.Type):
    __schema__ = shiphero_schema
    __field_names__ = ('request_id', 'complexity', 'shipping_plan')
    request_id = sgqlc.types.Field(String, graphql_name='request_id')

    complexity = sgqlc.types.Field(Int, graphql_name='complexity')

    shipping_plan = sgqlc.types.Field('ShippingPlan', graphql_name='shipping_plan')



class CreateVendorOutput(sgqlc.types.Type):
    __schema__ = shiphero_schema
    __field_names__ = ('request_id', 'complexity', 'vendor')
    request_id = sgqlc.types.Field(String, graphql_name='request_id')

    complexity = sgqlc.types.Field(Int, graphql_name='complexity')

    vendor = sgqlc.types.Field('Vendor', graphql_name='vendor')



class CreateWebhookOutput(sgqlc.types.Type):
    __schema__ = shiphero_schema
    __field_names__ = ('request_id', 'complexity', 'webhook')
    request_id = sgqlc.types.Field(String, graphql_name='request_id')

    complexity = sgqlc.types.Field(Int, graphql_name='complexity')

    webhook = sgqlc.types.Field('Webhook', graphql_name='webhook')



class CurrentUserQueryResult(sgqlc.types.Type):
    __schema__ = shiphero_schema
    __field_names__ = ('request_id', 'complexity', 'data')
    request_id = sgqlc.types.Field(String, graphql_name='request_id')

    complexity = sgqlc.types.Field(Int, graphql_name='complexity')

    data = sgqlc.types.Field('User', graphql_name='data')



class DeleteLotOutput(sgqlc.types.Type):
    __schema__ = shiphero_schema
    __field_names__ = ('request_id', 'complexity', 'lot')
    request_id = sgqlc.types.Field(String, graphql_name='request_id')

    complexity = sgqlc.types.Field(Int, graphql_name='complexity')

    lot = sgqlc.types.Field('Lot', graphql_name='lot')



class Dimensions(sgqlc.types.Type):
    __schema__ = shiphero_schema
    __field_names__ = ('weight', 'height', 'width', 'length')
    weight = sgqlc.types.Field(String, graphql_name='weight')

    height = sgqlc.types.Field(String, graphql_name='height')

    width = sgqlc.types.Field(String, graphql_name='width')

    length = sgqlc.types.Field(String, graphql_name='length')



class FeeCategoryTotal(sgqlc.types.Type):
    __schema__ = shiphero_schema
    __field_names__ = ('id', 'legacy_id', 'amount', 'label', 'category', 'quantity')
    id = sgqlc.types.Field(String, graphql_name='id')

    legacy_id = sgqlc.types.Field(Int, graphql_name='legacy_id')

    amount = sgqlc.types.Field(Money, graphql_name='amount')

    label = sgqlc.types.Field(String, graphql_name='label')

    category = sgqlc.types.Field(String, graphql_name='category')

    quantity = sgqlc.types.Field(Int, graphql_name='quantity')



class FeeCategoryTotalConnection(sgqlc.types.relay.Connection):
    __schema__ = shiphero_schema
    __field_names__ = ('page_info', 'edges')
    page_info = sgqlc.types.Field(sgqlc.types.non_null('PageInfo'), graphql_name='pageInfo')

    edges = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of('FeeCategoryTotalEdge')), graphql_name='edges')



class FeeCategoryTotalEdge(sgqlc.types.Type):
    __schema__ = shiphero_schema
    __field_names__ = ('node', 'cursor')
    node = sgqlc.types.Field(FeeCategoryTotal, graphql_name='node')

    cursor = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='cursor')



class FulfillmentInvoice(sgqlc.types.Type):
    __schema__ = shiphero_schema
    __field_names__ = ('id', 'legacy_id', 'stripe_charge_id', 'stripe_invoice_id', 'stripe_invoice_number', 'stripe_invoice_status', 'stripe_invoice_url', 'stripe_next_payment_attempt', 'account_id', 'cc_info', 'amount', 'created_at', 'shipping_items', 'inbound_shipping_items', 'returns_items', 'storage_items')
    id = sgqlc.types.Field(String, graphql_name='id')

    legacy_id = sgqlc.types.Field(Int, graphql_name='legacy_id')

    stripe_charge_id = sgqlc.types.Field(String, graphql_name='stripe_charge_id')

    stripe_invoice_id = sgqlc.types.Field(String, graphql_name='stripe_invoice_id')

    stripe_invoice_number = sgqlc.types.Field(String, graphql_name='stripe_invoice_number')

    stripe_invoice_status = sgqlc.types.Field(String, graphql_name='stripe_invoice_status')

    stripe_invoice_url = sgqlc.types.Field(String, graphql_name='stripe_invoice_url')

    stripe_next_payment_attempt = sgqlc.types.Field(ISODateTime, graphql_name='stripe_next_payment_attempt')

    account_id = sgqlc.types.Field(String, graphql_name='account_id')

    cc_info = sgqlc.types.Field(String, graphql_name='cc_info')

    amount = sgqlc.types.Field(String, graphql_name='amount')

    created_at = sgqlc.types.Field(ISODateTime, graphql_name='created_at')

    shipping_items = sgqlc.types.Field('FulfillmentInvoiceShippingItemConnection', graphql_name='shipping_items', args=sgqlc.types.ArgDict((
        ('sort', sgqlc.types.Arg(String, graphql_name='sort', default=None)),
        ('before', sgqlc.types.Arg(String, graphql_name='before', default=None)),
        ('after', sgqlc.types.Arg(String, graphql_name='after', default=None)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
))
    )
    '''Arguments:

    * `sort` (`String`)
    * `before` (`String`)
    * `after` (`String`)
    * `first` (`Int`)
    * `last` (`Int`)
    '''

    inbound_shipping_items = sgqlc.types.Field('FulfillmentInvoiceInboundShippingItemConnection', graphql_name='inbound_shipping_items', args=sgqlc.types.ArgDict((
        ('sort', sgqlc.types.Arg(String, graphql_name='sort', default=None)),
        ('before', sgqlc.types.Arg(String, graphql_name='before', default=None)),
        ('after', sgqlc.types.Arg(String, graphql_name='after', default=None)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
))
    )
    '''Arguments:

    * `sort` (`String`)
    * `before` (`String`)
    * `after` (`String`)
    * `first` (`Int`)
    * `last` (`Int`)
    '''

    returns_items = sgqlc.types.Field('FulfillmentInvoiceReturnItemConnection', graphql_name='returns_items', args=sgqlc.types.ArgDict((
        ('sort', sgqlc.types.Arg(String, graphql_name='sort', default=None)),
        ('before', sgqlc.types.Arg(String, graphql_name='before', default=None)),
        ('after', sgqlc.types.Arg(String, graphql_name='after', default=None)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
))
    )
    '''Arguments:

    * `sort` (`String`)
    * `before` (`String`)
    * `after` (`String`)
    * `first` (`Int`)
    * `last` (`Int`)
    '''

    storage_items = sgqlc.types.Field('FulfillmentInvoiceStorageItemConnection', graphql_name='storage_items', args=sgqlc.types.ArgDict((
        ('sort', sgqlc.types.Arg(String, graphql_name='sort', default=None)),
        ('before', sgqlc.types.Arg(String, graphql_name='before', default=None)),
        ('after', sgqlc.types.Arg(String, graphql_name='after', default=None)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
))
    )
    '''Arguments:

    * `sort` (`String`)
    * `before` (`String`)
    * `after` (`String`)
    * `first` (`Int`)
    * `last` (`Int`)
    '''



class FulfillmentInvoiceConnection(sgqlc.types.relay.Connection):
    __schema__ = shiphero_schema
    __field_names__ = ('page_info', 'edges')
    page_info = sgqlc.types.Field(sgqlc.types.non_null('PageInfo'), graphql_name='pageInfo')

    edges = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of('FulfillmentInvoiceEdge')), graphql_name='edges')



class FulfillmentInvoiceEdge(sgqlc.types.Type):
    __schema__ = shiphero_schema
    __field_names__ = ('node', 'cursor')
    node = sgqlc.types.Field(FulfillmentInvoice, graphql_name='node')

    cursor = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='cursor')



class FulfillmentInvoiceInboundShippingItem(sgqlc.types.Type):
    __schema__ = shiphero_schema
    __field_names__ = ('id', 'legacy_id', 'account_id', 'invoice_id', 'purchase_order_id', 'shipment_id', 'shipping_label_id', 'amount', 'cost', 'created_at')
    id = sgqlc.types.Field(String, graphql_name='id')

    legacy_id = sgqlc.types.Field(Int, graphql_name='legacy_id')

    account_id = sgqlc.types.Field(String, graphql_name='account_id')

    invoice_id = sgqlc.types.Field(String, graphql_name='invoice_id')

    purchase_order_id = sgqlc.types.Field(String, graphql_name='purchase_order_id')

    shipment_id = sgqlc.types.Field(String, graphql_name='shipment_id')

    shipping_label_id = sgqlc.types.Field(String, graphql_name='shipping_label_id')

    amount = sgqlc.types.Field(String, graphql_name='amount')

    cost = sgqlc.types.Field(String, graphql_name='cost')

    created_at = sgqlc.types.Field(ISODateTime, graphql_name='created_at')



class FulfillmentInvoiceInboundShippingItemConnection(sgqlc.types.relay.Connection):
    __schema__ = shiphero_schema
    __field_names__ = ('page_info', 'edges')
    page_info = sgqlc.types.Field(sgqlc.types.non_null('PageInfo'), graphql_name='pageInfo')

    edges = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of('FulfillmentInvoiceInboundShippingItemEdge')), graphql_name='edges')



class FulfillmentInvoiceInboundShippingItemEdge(sgqlc.types.Type):
    __schema__ = shiphero_schema
    __field_names__ = ('node', 'cursor')
    node = sgqlc.types.Field(FulfillmentInvoiceInboundShippingItem, graphql_name='node')

    cursor = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='cursor')



class FulfillmentInvoiceQueryResult(sgqlc.types.Type):
    __schema__ = shiphero_schema
    __field_names__ = ('request_id', 'complexity', 'data')
    request_id = sgqlc.types.Field(String, graphql_name='request_id')

    complexity = sgqlc.types.Field(Int, graphql_name='complexity')

    data = sgqlc.types.Field(FulfillmentInvoice, graphql_name='data')



class FulfillmentInvoiceReturnItem(sgqlc.types.Type):
    __schema__ = shiphero_schema
    __field_names__ = ('id', 'legacy_id', 'account_id', 'invoice_id', 'order_id', 'rma_id', 'rma_label_id', 'amount', 'shipping_rate', 'picking_fee', 'inspection_fee', 'restocking_fee', 'created_at')
    id = sgqlc.types.Field(String, graphql_name='id')

    legacy_id = sgqlc.types.Field(Int, graphql_name='legacy_id')

    account_id = sgqlc.types.Field(String, graphql_name='account_id')

    invoice_id = sgqlc.types.Field(String, graphql_name='invoice_id')

    order_id = sgqlc.types.Field(String, graphql_name='order_id')

    rma_id = sgqlc.types.Field(String, graphql_name='rma_id')

    rma_label_id = sgqlc.types.Field(String, graphql_name='rma_label_id')

    amount = sgqlc.types.Field(String, graphql_name='amount')

    shipping_rate = sgqlc.types.Field(String, graphql_name='shipping_rate')

    picking_fee = sgqlc.types.Field(String, graphql_name='picking_fee')

    inspection_fee = sgqlc.types.Field(String, graphql_name='inspection_fee')

    restocking_fee = sgqlc.types.Field(String, graphql_name='restocking_fee')

    created_at = sgqlc.types.Field(ISODateTime, graphql_name='created_at')



class FulfillmentInvoiceReturnItemConnection(sgqlc.types.relay.Connection):
    __schema__ = shiphero_schema
    __field_names__ = ('page_info', 'edges')
    page_info = sgqlc.types.Field(sgqlc.types.non_null('PageInfo'), graphql_name='pageInfo')

    edges = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of('FulfillmentInvoiceReturnItemEdge')), graphql_name='edges')



class FulfillmentInvoiceReturnItemEdge(sgqlc.types.Type):
    __schema__ = shiphero_schema
    __field_names__ = ('node', 'cursor')
    node = sgqlc.types.Field(FulfillmentInvoiceReturnItem, graphql_name='node')

    cursor = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='cursor')



class FulfillmentInvoiceShippingItem(sgqlc.types.Type):
    __schema__ = shiphero_schema
    __field_names__ = ('id', 'legacy_id', 'account_id', 'invoice_id', 'order_id', 'shipment_id', 'shipping_label_id', 'amount', 'shipping_rate', 'processing_fee', 'picking_fee', 'overcharge_fee', 'created_at')
    id = sgqlc.types.Field(String, graphql_name='id')

    legacy_id = sgqlc.types.Field(Int, graphql_name='legacy_id')

    account_id = sgqlc.types.Field(String, graphql_name='account_id')

    invoice_id = sgqlc.types.Field(String, graphql_name='invoice_id')

    order_id = sgqlc.types.Field(String, graphql_name='order_id')

    shipment_id = sgqlc.types.Field(String, graphql_name='shipment_id')

    shipping_label_id = sgqlc.types.Field(String, graphql_name='shipping_label_id')

    amount = sgqlc.types.Field(String, graphql_name='amount')

    shipping_rate = sgqlc.types.Field(String, graphql_name='shipping_rate')

    processing_fee = sgqlc.types.Field(String, graphql_name='processing_fee')

    picking_fee = sgqlc.types.Field(String, graphql_name='picking_fee')

    overcharge_fee = sgqlc.types.Field(String, graphql_name='overcharge_fee')

    created_at = sgqlc.types.Field(ISODateTime, graphql_name='created_at')



class FulfillmentInvoiceShippingItemConnection(sgqlc.types.relay.Connection):
    __schema__ = shiphero_schema
    __field_names__ = ('page_info', 'edges')
    page_info = sgqlc.types.Field(sgqlc.types.non_null('PageInfo'), graphql_name='pageInfo')

    edges = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of('FulfillmentInvoiceShippingItemEdge')), graphql_name='edges')



class FulfillmentInvoiceShippingItemEdge(sgqlc.types.Type):
    __schema__ = shiphero_schema
    __field_names__ = ('node', 'cursor')
    node = sgqlc.types.Field(FulfillmentInvoiceShippingItem, graphql_name='node')

    cursor = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='cursor')



class FulfillmentInvoiceStorageItem(sgqlc.types.Type):
    __schema__ = shiphero_schema
    __field_names__ = ('id', 'legacy_id', 'account_id', 'warehouse_id', 'invoice_id', 'amount', 'created_at')
    id = sgqlc.types.Field(String, graphql_name='id')

    legacy_id = sgqlc.types.Field(Int, graphql_name='legacy_id')

    account_id = sgqlc.types.Field(String, graphql_name='account_id')

    warehouse_id = sgqlc.types.Field(String, graphql_name='warehouse_id')

    invoice_id = sgqlc.types.Field(String, graphql_name='invoice_id')

    amount = sgqlc.types.Field(String, graphql_name='amount')

    created_at = sgqlc.types.Field(ISODateTime, graphql_name='created_at')



class FulfillmentInvoiceStorageItemConnection(sgqlc.types.relay.Connection):
    __schema__ = shiphero_schema
    __field_names__ = ('page_info', 'edges')
    page_info = sgqlc.types.Field(sgqlc.types.non_null('PageInfo'), graphql_name='pageInfo')

    edges = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of('FulfillmentInvoiceStorageItemEdge')), graphql_name='edges')



class FulfillmentInvoiceStorageItemEdge(sgqlc.types.Type):
    __schema__ = shiphero_schema
    __field_names__ = ('node', 'cursor')
    node = sgqlc.types.Field(FulfillmentInvoiceStorageItem, graphql_name='node')

    cursor = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='cursor')



class FulfillmentInvoicesQueryResult(sgqlc.types.Type):
    __schema__ = shiphero_schema
    __field_names__ = ('request_id', 'complexity', 'data')
    request_id = sgqlc.types.Field(String, graphql_name='request_id')

    complexity = sgqlc.types.Field(Int, graphql_name='complexity')

    data = sgqlc.types.Field(FulfillmentInvoiceConnection, graphql_name='data', args=sgqlc.types.ArgDict((
        ('sort', sgqlc.types.Arg(String, graphql_name='sort', default=None)),
        ('before', sgqlc.types.Arg(String, graphql_name='before', default=None)),
        ('after', sgqlc.types.Arg(String, graphql_name='after', default=None)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
))
    )
    '''Arguments:

    * `sort` (`String`)
    * `before` (`String`)
    * `after` (`String`)
    * `first` (`Int`)
    * `last` (`Int`)
    '''



class InventoryChange(sgqlc.types.Type):
    __schema__ = shiphero_schema
    __field_names__ = ('user_id', 'account_id', 'warehouse_id', 'sku', 'previous_on_hand', 'change_in_on_hand', 'reason', 'cycle_counted', 'location_id', 'created_at', 'location')
    user_id = sgqlc.types.Field(String, graphql_name='user_id')

    account_id = sgqlc.types.Field(String, graphql_name='account_id')

    warehouse_id = sgqlc.types.Field(String, graphql_name='warehouse_id')

    sku = sgqlc.types.Field(String, graphql_name='sku')

    previous_on_hand = sgqlc.types.Field(Int, graphql_name='previous_on_hand')

    change_in_on_hand = sgqlc.types.Field(Int, graphql_name='change_in_on_hand')

    reason = sgqlc.types.Field(String, graphql_name='reason')

    cycle_counted = sgqlc.types.Field(Boolean, graphql_name='cycle_counted')

    location_id = sgqlc.types.Field(String, graphql_name='location_id')

    created_at = sgqlc.types.Field(ISODateTime, graphql_name='created_at')

    location = sgqlc.types.Field('Location', graphql_name='location')



class InventoryChangeConnection(sgqlc.types.relay.Connection):
    __schema__ = shiphero_schema
    __field_names__ = ('page_info', 'edges')
    page_info = sgqlc.types.Field(sgqlc.types.non_null('PageInfo'), graphql_name='pageInfo')

    edges = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of('InventoryChangeEdge')), graphql_name='edges')



class InventoryChangeEdge(sgqlc.types.Type):
    __schema__ = shiphero_schema
    __field_names__ = ('node', 'cursor')
    node = sgqlc.types.Field(InventoryChange, graphql_name='node')

    cursor = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='cursor')



class InventoryChangesQueryResult(sgqlc.types.Type):
    __schema__ = shiphero_schema
    __field_names__ = ('request_id', 'complexity', 'data')
    request_id = sgqlc.types.Field(String, graphql_name='request_id')

    complexity = sgqlc.types.Field(Int, graphql_name='complexity')

    data = sgqlc.types.Field(InventoryChangeConnection, graphql_name='data', args=sgqlc.types.ArgDict((
        ('sort', sgqlc.types.Arg(String, graphql_name='sort', default=None)),
        ('before', sgqlc.types.Arg(String, graphql_name='before', default=None)),
        ('after', sgqlc.types.Arg(String, graphql_name='after', default=None)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
))
    )
    '''Arguments:

    * `sort` (`String`)
    * `before` (`String`)
    * `after` (`String`)
    * `first` (`Int`)
    * `last` (`Int`)
    '''



class InventorySnapshot(sgqlc.types.Type):
    __schema__ = shiphero_schema
    __field_names__ = ('snapshot_id', 'job_user_id', 'job_account_id', 'warehouse_id', 'customer_account_id', 'notification_email', 'email_error', 'post_url', 'post_error', 'post_url_pre_check', 'status', 'error', 'created_at', 'enqueued_at', 'updated_at', 'snapshot_url', 'snapshot_expiration', 'new_format')
    snapshot_id = sgqlc.types.Field(String, graphql_name='snapshot_id')

    job_user_id = sgqlc.types.Field(String, graphql_name='job_user_id')

    job_account_id = sgqlc.types.Field(String, graphql_name='job_account_id')

    warehouse_id = sgqlc.types.Field(String, graphql_name='warehouse_id')

    customer_account_id = sgqlc.types.Field(String, graphql_name='customer_account_id')

    notification_email = sgqlc.types.Field(String, graphql_name='notification_email')

    email_error = sgqlc.types.Field(String, graphql_name='email_error')

    post_url = sgqlc.types.Field(String, graphql_name='post_url')

    post_error = sgqlc.types.Field(String, graphql_name='post_error')

    post_url_pre_check = sgqlc.types.Field(Boolean, graphql_name='post_url_pre_check')

    status = sgqlc.types.Field(String, graphql_name='status')

    error = sgqlc.types.Field(String, graphql_name='error')

    created_at = sgqlc.types.Field(ISODateTime, graphql_name='created_at')

    enqueued_at = sgqlc.types.Field(ISODateTime, graphql_name='enqueued_at')

    updated_at = sgqlc.types.Field(ISODateTime, graphql_name='updated_at')

    snapshot_url = sgqlc.types.Field(String, graphql_name='snapshot_url')

    snapshot_expiration = sgqlc.types.Field(ISODateTime, graphql_name='snapshot_expiration')

    new_format = sgqlc.types.Field(Boolean, graphql_name='new_format')



class InventorySnapshotConnection(sgqlc.types.relay.Connection):
    __schema__ = shiphero_schema
    __field_names__ = ('page_info', 'edges')
    page_info = sgqlc.types.Field(sgqlc.types.non_null('PageInfo'), graphql_name='pageInfo')

    edges = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of('InventorySnapshotEdge')), graphql_name='edges')



class InventorySnapshotEdge(sgqlc.types.Type):
    __schema__ = shiphero_schema
    __field_names__ = ('node', 'cursor')
    node = sgqlc.types.Field(InventorySnapshot, graphql_name='node')

    cursor = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='cursor')



class InventorySnapshotOutput(sgqlc.types.Type):
    __schema__ = shiphero_schema
    __field_names__ = ('request_id', 'complexity', 'snapshot')
    request_id = sgqlc.types.Field(String, graphql_name='request_id')

    complexity = sgqlc.types.Field(Int, graphql_name='complexity')

    snapshot = sgqlc.types.Field(InventorySnapshot, graphql_name='snapshot')



class InventorySnapshotQueryResult(sgqlc.types.Type):
    __schema__ = shiphero_schema
    __field_names__ = ('request_id', 'complexity', 'snapshot')
    request_id = sgqlc.types.Field(String, graphql_name='request_id')

    complexity = sgqlc.types.Field(Int, graphql_name='complexity')

    snapshot = sgqlc.types.Field(InventorySnapshot, graphql_name='snapshot')



class InventorySnapshotsQueryResult(sgqlc.types.Type):
    __schema__ = shiphero_schema
    __field_names__ = ('request_id', 'complexity', 'snapshots')
    request_id = sgqlc.types.Field(String, graphql_name='request_id')

    complexity = sgqlc.types.Field(Int, graphql_name='complexity')

    snapshots = sgqlc.types.Field(InventorySnapshotConnection, graphql_name='snapshots', args=sgqlc.types.ArgDict((
        ('sort', sgqlc.types.Arg(String, graphql_name='sort', default=None)),
        ('before', sgqlc.types.Arg(String, graphql_name='before', default=None)),
        ('after', sgqlc.types.Arg(String, graphql_name='after', default=None)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
))
    )
    '''Arguments:

    * `sort` (`String`)
    * `before` (`String`)
    * `after` (`String`)
    * `first` (`Int`)
    * `last` (`Int`)
    '''



class InventorySyncBatchQueryResult(sgqlc.types.Type):
    __schema__ = shiphero_schema
    __field_names__ = ('request_id', 'complexity', 'data')
    request_id = sgqlc.types.Field(String, graphql_name='request_id')

    complexity = sgqlc.types.Field(Int, graphql_name='complexity')

    data = sgqlc.types.Field('InventorySyncStatus', graphql_name='data')



class InventorySyncBatchesQueryResult(sgqlc.types.Type):
    __schema__ = shiphero_schema
    __field_names__ = ('request_id', 'complexity', 'data')
    request_id = sgqlc.types.Field(String, graphql_name='request_id')

    complexity = sgqlc.types.Field(Int, graphql_name='complexity')

    data = sgqlc.types.Field('InventorySyncStatusConnection', graphql_name='data', args=sgqlc.types.ArgDict((
        ('sort', sgqlc.types.Arg(String, graphql_name='sort', default=None)),
        ('before', sgqlc.types.Arg(String, graphql_name='before', default=None)),
        ('after', sgqlc.types.Arg(String, graphql_name='after', default=None)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
))
    )
    '''Arguments:

    * `sort` (`String`)
    * `before` (`String`)
    * `after` (`String`)
    * `first` (`Int`)
    * `last` (`Int`)
    '''



class InventorySyncItemStatus(sgqlc.types.Type):
    __schema__ = shiphero_schema
    __field_names__ = ('id', 'row', 'sku', 'quantity', 'action', 'reason', 'location', 'status', 'error', 'created_at', 'updated_at')
    id = sgqlc.types.Field(String, graphql_name='id')

    row = sgqlc.types.Field(Int, graphql_name='row')

    sku = sgqlc.types.Field(String, graphql_name='sku')

    quantity = sgqlc.types.Field(Int, graphql_name='quantity')

    action = sgqlc.types.Field(String, graphql_name='action')

    reason = sgqlc.types.Field(String, graphql_name='reason')

    location = sgqlc.types.Field(Int, graphql_name='location')

    status = sgqlc.types.Field(String, graphql_name='status')

    error = sgqlc.types.Field(String, graphql_name='error')

    created_at = sgqlc.types.Field(ISODateTime, graphql_name='created_at')

    updated_at = sgqlc.types.Field(ISODateTime, graphql_name='updated_at')



class InventorySyncItemStatusConnection(sgqlc.types.relay.Connection):
    __schema__ = shiphero_schema
    __field_names__ = ('page_info', 'edges')
    page_info = sgqlc.types.Field(sgqlc.types.non_null('PageInfo'), graphql_name='pageInfo')

    edges = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of('InventorySyncItemStatusEdge')), graphql_name='edges')



class InventorySyncItemStatusEdge(sgqlc.types.Type):
    __schema__ = shiphero_schema
    __field_names__ = ('node', 'cursor')
    node = sgqlc.types.Field(InventorySyncItemStatus, graphql_name='node')

    cursor = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='cursor')



class InventorySyncOutput(sgqlc.types.Type):
    __schema__ = shiphero_schema
    __field_names__ = ('request_id', 'complexity', 'sync_id')
    request_id = sgqlc.types.Field(String, graphql_name='request_id')

    complexity = sgqlc.types.Field(Int, graphql_name='complexity')

    sync_id = sgqlc.types.Field(String, graphql_name='sync_id')



class InventorySyncRowsQueryResult(sgqlc.types.Type):
    __schema__ = shiphero_schema
    __field_names__ = ('request_id', 'complexity', 'data')
    request_id = sgqlc.types.Field(String, graphql_name='request_id')

    complexity = sgqlc.types.Field(Int, graphql_name='complexity')

    data = sgqlc.types.Field(InventorySyncItemStatusConnection, graphql_name='data', args=sgqlc.types.ArgDict((
        ('sort', sgqlc.types.Arg(String, graphql_name='sort', default=None)),
        ('before', sgqlc.types.Arg(String, graphql_name='before', default=None)),
        ('after', sgqlc.types.Arg(String, graphql_name='after', default=None)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
))
    )
    '''Arguments:

    * `sort` (`String`)
    * `before` (`String`)
    * `after` (`String`)
    * `first` (`Int`)
    * `last` (`Int`)
    '''



class InventorySyncStatus(sgqlc.types.Type):
    __schema__ = shiphero_schema
    __field_names__ = ('id', 'url', 'user_id', 'account_id', 'warehouse_id', 'customer_account_id', 'total_count', 'status', 'error', 'created_at', 'updated_at', 'success_count', 'error_count', 'finished_count')
    id = sgqlc.types.Field(String, graphql_name='id')

    url = sgqlc.types.Field(String, graphql_name='url')

    user_id = sgqlc.types.Field(String, graphql_name='user_id')

    account_id = sgqlc.types.Field(String, graphql_name='account_id')

    warehouse_id = sgqlc.types.Field(String, graphql_name='warehouse_id')

    customer_account_id = sgqlc.types.Field(String, graphql_name='customer_account_id')

    total_count = sgqlc.types.Field(Int, graphql_name='total_count')

    status = sgqlc.types.Field(String, graphql_name='status')

    error = sgqlc.types.Field(String, graphql_name='error')

    created_at = sgqlc.types.Field(ISODateTime, graphql_name='created_at')

    updated_at = sgqlc.types.Field(ISODateTime, graphql_name='updated_at')

    success_count = sgqlc.types.Field(Int, graphql_name='success_count')

    error_count = sgqlc.types.Field(Int, graphql_name='error_count')

    finished_count = sgqlc.types.Field(Int, graphql_name='finished_count')



class InventorySyncStatusConnection(sgqlc.types.relay.Connection):
    __schema__ = shiphero_schema
    __field_names__ = ('page_info', 'edges')
    page_info = sgqlc.types.Field(sgqlc.types.non_null('PageInfo'), graphql_name='pageInfo')

    edges = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of('InventorySyncStatusEdge')), graphql_name='edges')



class InventorySyncStatusEdge(sgqlc.types.Type):
    __schema__ = shiphero_schema
    __field_names__ = ('node', 'cursor')
    node = sgqlc.types.Field(InventorySyncStatus, graphql_name='node')

    cursor = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='cursor')



class ItemLocation(sgqlc.types.Type):
    __schema__ = shiphero_schema
    __field_names__ = ('id', 'legacy_id', 'account_id', 'warehouse_id', 'location_id', 'sku', 'quantity', 'created_at', 'location', 'expiration_lot')
    id = sgqlc.types.Field(String, graphql_name='id')

    legacy_id = sgqlc.types.Field(Int, graphql_name='legacy_id')

    account_id = sgqlc.types.Field(String, graphql_name='account_id')

    warehouse_id = sgqlc.types.Field(String, graphql_name='warehouse_id')

    location_id = sgqlc.types.Field(String, graphql_name='location_id')

    sku = sgqlc.types.Field(String, graphql_name='sku')

    quantity = sgqlc.types.Field(Int, graphql_name='quantity')

    created_at = sgqlc.types.Field(ISODateTime, graphql_name='created_at')

    location = sgqlc.types.Field('Location', graphql_name='location')

    expiration_lot = sgqlc.types.Field('Lot', graphql_name='expiration_lot')



class ItemLocationConnection(sgqlc.types.relay.Connection):
    __schema__ = shiphero_schema
    __field_names__ = ('page_info', 'edges')
    page_info = sgqlc.types.Field(sgqlc.types.non_null('PageInfo'), graphql_name='pageInfo')

    edges = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of('ItemLocationEdge')), graphql_name='edges')



class ItemLocationEdge(sgqlc.types.Type):
    __schema__ = shiphero_schema
    __field_names__ = ('node', 'cursor')
    node = sgqlc.types.Field(ItemLocation, graphql_name='node')

    cursor = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='cursor')



class KitComponent(sgqlc.types.Type):
    __schema__ = shiphero_schema
    __field_names__ = ('id', 'legacy_id', 'account_id', 'sku', 'quantity')
    id = sgqlc.types.Field(String, graphql_name='id')

    legacy_id = sgqlc.types.Field(Int, graphql_name='legacy_id')

    account_id = sgqlc.types.Field(String, graphql_name='account_id')

    sku = sgqlc.types.Field(String, graphql_name='sku')

    quantity = sgqlc.types.Field(Int, graphql_name='quantity')



class LabelResource(sgqlc.types.Type):
    __schema__ = shiphero_schema
    __field_names__ = ('pdf_location', 'paper_pdf_location', 'thermal_pdf_location', 'image_location')
    pdf_location = sgqlc.types.Field(String, graphql_name='pdf_location')

    paper_pdf_location = sgqlc.types.Field(String, graphql_name='paper_pdf_location')

    thermal_pdf_location = sgqlc.types.Field(String, graphql_name='thermal_pdf_location')

    image_location = sgqlc.types.Field(String, graphql_name='image_location')



class LegacyId(sgqlc.types.Type):
    __schema__ = shiphero_schema
    __field_names__ = ('legacy_id', 'id')
    legacy_id = sgqlc.types.Field(Int, graphql_name='legacy_id')

    id = sgqlc.types.Field(String, graphql_name='id')



class LegacyIdQueryResult(sgqlc.types.Type):
    __schema__ = shiphero_schema
    __field_names__ = ('request_id', 'complexity', 'data')
    request_id = sgqlc.types.Field(String, graphql_name='request_id')

    complexity = sgqlc.types.Field(Int, graphql_name='complexity')

    data = sgqlc.types.Field(LegacyId, graphql_name='data')



class LineItem(sgqlc.types.Type):
    __schema__ = shiphero_schema
    __field_names__ = ('id', 'legacy_id', 'sku', 'partner_line_item_id', 'quantity', 'price', 'product_name', 'option_title', 'fulfillment_status', 'quantity_pending_fulfillment', 'quantity_shipped', 'warehouse', 'quantity_allocated', 'backorder_quantity', 'custom_options', 'custom_barcode', 'eligible_for_return', 'customs_value', 'locked_to_warehouse_id', 'subtotal', 'barcode', 'created_at', 'updated_at', 'order_id', 'shipped_line_item_lots', 'serial_numbers', 'promotion_discount', 'product', 'tote_picks')
    id = sgqlc.types.Field(String, graphql_name='id')

    legacy_id = sgqlc.types.Field(Int, graphql_name='legacy_id')

    sku = sgqlc.types.Field(String, graphql_name='sku')

    partner_line_item_id = sgqlc.types.Field(String, graphql_name='partner_line_item_id')

    quantity = sgqlc.types.Field(Int, graphql_name='quantity')

    price = sgqlc.types.Field(String, graphql_name='price')

    product_name = sgqlc.types.Field(String, graphql_name='product_name')

    option_title = sgqlc.types.Field(String, graphql_name='option_title')

    fulfillment_status = sgqlc.types.Field(String, graphql_name='fulfillment_status')

    quantity_pending_fulfillment = sgqlc.types.Field(Int, graphql_name='quantity_pending_fulfillment')

    quantity_shipped = sgqlc.types.Field(Int, graphql_name='quantity_shipped')

    warehouse = sgqlc.types.Field(String, graphql_name='warehouse')

    quantity_allocated = sgqlc.types.Field(Int, graphql_name='quantity_allocated')

    backorder_quantity = sgqlc.types.Field(Int, graphql_name='backorder_quantity')

    custom_options = sgqlc.types.Field(GenericScalar, graphql_name='custom_options')

    custom_barcode = sgqlc.types.Field(String, graphql_name='custom_barcode')

    eligible_for_return = sgqlc.types.Field(Boolean, graphql_name='eligible_for_return')

    customs_value = sgqlc.types.Field(String, graphql_name='customs_value')

    locked_to_warehouse_id = sgqlc.types.Field(String, graphql_name='locked_to_warehouse_id')

    subtotal = sgqlc.types.Field(String, graphql_name='subtotal')

    barcode = sgqlc.types.Field(String, graphql_name='barcode')

    created_at = sgqlc.types.Field(ISODateTime, graphql_name='created_at')

    updated_at = sgqlc.types.Field(ISODateTime, graphql_name='updated_at')

    order_id = sgqlc.types.Field(String, graphql_name='order_id')

    shipped_line_item_lots = sgqlc.types.Field(sgqlc.types.list_of('ShippedLineItemLot'), graphql_name='shipped_line_item_lots')

    serial_numbers = sgqlc.types.Field(sgqlc.types.list_of('LineItemSerialNumber'), graphql_name='serial_numbers')

    promotion_discount = sgqlc.types.Field(String, graphql_name='promotion_discount')

    product = sgqlc.types.Field('Product', graphql_name='product')

    tote_picks = sgqlc.types.Field(sgqlc.types.list_of('TotePick'), graphql_name='tote_picks')



class LineItemConnection(sgqlc.types.relay.Connection):
    __schema__ = shiphero_schema
    __field_names__ = ('page_info', 'edges')
    page_info = sgqlc.types.Field(sgqlc.types.non_null('PageInfo'), graphql_name='pageInfo')

    edges = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of('LineItemEdge')), graphql_name='edges')



class LineItemEdge(sgqlc.types.Type):
    __schema__ = shiphero_schema
    __field_names__ = ('node', 'cursor')
    node = sgqlc.types.Field(LineItem, graphql_name='node')

    cursor = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='cursor')



class LineItemSerialNumber(sgqlc.types.Type):
    __schema__ = shiphero_schema
    __field_names__ = ('id', 'legacy_id', 'line_item_id', 'serial_number', 'scanned', 'created_at', 'updated_at')
    id = sgqlc.types.Field(String, graphql_name='id')

    legacy_id = sgqlc.types.Field(Int, graphql_name='legacy_id')

    line_item_id = sgqlc.types.Field(String, graphql_name='line_item_id')

    serial_number = sgqlc.types.Field(String, graphql_name='serial_number')

    scanned = sgqlc.types.Field(Boolean, graphql_name='scanned')

    created_at = sgqlc.types.Field(ISODateTime, graphql_name='created_at')

    updated_at = sgqlc.types.Field(ISODateTime, graphql_name='updated_at')



class Location(sgqlc.types.Type):
    __schema__ = shiphero_schema
    __field_names__ = ('id', 'legacy_id', 'account_id', 'warehouse_id', 'type', 'name', 'zone', 'pickable', 'sellable', 'is_cart', 'pick_priority', 'dimensions', 'temperature', 'last_counted', 'created_at', 'expiration_lots')
    id = sgqlc.types.Field(String, graphql_name='id')

    legacy_id = sgqlc.types.Field(Int, graphql_name='legacy_id')

    account_id = sgqlc.types.Field(String, graphql_name='account_id')

    warehouse_id = sgqlc.types.Field(String, graphql_name='warehouse_id')

    type = sgqlc.types.Field('LocationType', graphql_name='type')

    name = sgqlc.types.Field(String, graphql_name='name')

    zone = sgqlc.types.Field(String, graphql_name='zone')

    pickable = sgqlc.types.Field(Boolean, graphql_name='pickable')

    sellable = sgqlc.types.Field(Boolean, graphql_name='sellable')

    is_cart = sgqlc.types.Field(Boolean, graphql_name='is_cart')

    pick_priority = sgqlc.types.Field(Int, graphql_name='pick_priority')

    dimensions = sgqlc.types.Field(Dimensions, graphql_name='dimensions')

    temperature = sgqlc.types.Field(String, graphql_name='temperature')

    last_counted = sgqlc.types.Field(ISODateTime, graphql_name='last_counted')

    created_at = sgqlc.types.Field(ISODateTime, graphql_name='created_at')

    expiration_lots = sgqlc.types.Field('LotConnection', graphql_name='expiration_lots', args=sgqlc.types.ArgDict((
        ('customer_account_id', sgqlc.types.Arg(String, graphql_name='customer_account_id', default=None)),
        ('sort', sgqlc.types.Arg(String, graphql_name='sort', default=None)),
        ('before', sgqlc.types.Arg(String, graphql_name='before', default=None)),
        ('after', sgqlc.types.Arg(String, graphql_name='after', default=None)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
))
    )
    '''Arguments:

    * `customer_account_id` (`String`)
    * `sort` (`String`)
    * `before` (`String`)
    * `after` (`String`)
    * `first` (`Int`)
    * `last` (`Int`)
    '''



class LocationConnection(sgqlc.types.relay.Connection):
    __schema__ = shiphero_schema
    __field_names__ = ('page_info', 'edges')
    page_info = sgqlc.types.Field(sgqlc.types.non_null('PageInfo'), graphql_name='pageInfo')

    edges = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of('LocationEdge')), graphql_name='edges')



class LocationEdge(sgqlc.types.Type):
    __schema__ = shiphero_schema
    __field_names__ = ('node', 'cursor')
    node = sgqlc.types.Field(Location, graphql_name='node')

    cursor = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='cursor')



class LocationOutput(sgqlc.types.Type):
    __schema__ = shiphero_schema
    __field_names__ = ('request_id', 'complexity', 'location')
    request_id = sgqlc.types.Field(String, graphql_name='request_id')

    complexity = sgqlc.types.Field(Int, graphql_name='complexity')

    location = sgqlc.types.Field(Location, graphql_name='location')



class LocationQueryResult(sgqlc.types.Type):
    __schema__ = shiphero_schema
    __field_names__ = ('request_id', 'complexity', 'data')
    request_id = sgqlc.types.Field(String, graphql_name='request_id')

    complexity = sgqlc.types.Field(Int, graphql_name='complexity')

    data = sgqlc.types.Field(Location, graphql_name='data')



class LocationType(sgqlc.types.Type):
    __schema__ = shiphero_schema
    __field_names__ = ('id', 'legacy_id', 'account_id', 'name', 'daily_storage_cost')
    id = sgqlc.types.Field(String, graphql_name='id')

    legacy_id = sgqlc.types.Field(Int, graphql_name='legacy_id')

    account_id = sgqlc.types.Field(String, graphql_name='account_id')

    name = sgqlc.types.Field(String, graphql_name='name')

    daily_storage_cost = sgqlc.types.Field(String, graphql_name='daily_storage_cost')



class LocationsQueryResult(sgqlc.types.Type):
    __schema__ = shiphero_schema
    __field_names__ = ('request_id', 'complexity', 'data')
    request_id = sgqlc.types.Field(String, graphql_name='request_id')

    complexity = sgqlc.types.Field(Int, graphql_name='complexity')

    data = sgqlc.types.Field(LocationConnection, graphql_name='data', args=sgqlc.types.ArgDict((
        ('sort', sgqlc.types.Arg(String, graphql_name='sort', default=None)),
        ('before', sgqlc.types.Arg(String, graphql_name='before', default=None)),
        ('after', sgqlc.types.Arg(String, graphql_name='after', default=None)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
))
    )
    '''Arguments:

    * `sort` (`String`)
    * `before` (`String`)
    * `after` (`String`)
    * `first` (`Int`)
    * `last` (`Int`)
    '''



class Lot(sgqlc.types.Type):
    __schema__ = shiphero_schema
    __field_names__ = ('id', 'legacy_id', 'account_id', 'po_id', 'name', 'sku', 'created_at', 'updated_at', 'expires_at', 'received_at', 'is_active')
    id = sgqlc.types.Field(String, graphql_name='id')

    legacy_id = sgqlc.types.Field(Int, graphql_name='legacy_id')

    account_id = sgqlc.types.Field(String, graphql_name='account_id')

    po_id = sgqlc.types.Field(String, graphql_name='po_id')

    name = sgqlc.types.Field(String, graphql_name='name')

    sku = sgqlc.types.Field(String, graphql_name='sku')

    created_at = sgqlc.types.Field(ISODateTime, graphql_name='created_at')

    updated_at = sgqlc.types.Field(ISODateTime, graphql_name='updated_at')

    expires_at = sgqlc.types.Field(ISODateTime, graphql_name='expires_at')

    received_at = sgqlc.types.Field(ISODateTime, graphql_name='received_at')

    is_active = sgqlc.types.Field(Boolean, graphql_name='is_active')



class LotConnection(sgqlc.types.relay.Connection):
    __schema__ = shiphero_schema
    __field_names__ = ('page_info', 'edges')
    page_info = sgqlc.types.Field(sgqlc.types.non_null('PageInfo'), graphql_name='pageInfo')

    edges = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of('LotEdge')), graphql_name='edges')



class LotEdge(sgqlc.types.Type):
    __schema__ = shiphero_schema
    __field_names__ = ('node', 'cursor')
    node = sgqlc.types.Field(Lot, graphql_name='node')

    cursor = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='cursor')



class LotsQueryResult(sgqlc.types.Type):
    __schema__ = shiphero_schema
    __field_names__ = ('request_id', 'complexity', 'data')
    request_id = sgqlc.types.Field(String, graphql_name='request_id')

    complexity = sgqlc.types.Field(Int, graphql_name='complexity')

    data = sgqlc.types.Field(LotConnection, graphql_name='data', args=sgqlc.types.ArgDict((
        ('sort', sgqlc.types.Arg(String, graphql_name='sort', default=None)),
        ('before', sgqlc.types.Arg(String, graphql_name='before', default=None)),
        ('after', sgqlc.types.Arg(String, graphql_name='after', default=None)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
))
    )
    '''Arguments:

    * `sort` (`String`)
    * `before` (`String`)
    * `after` (`String`)
    * `first` (`Int`)
    * `last` (`Int`)
    '''



class MergedOrder(sgqlc.types.Type):
    __schema__ = shiphero_schema
    __field_names__ = ('order_id', 'is_master')
    order_id = sgqlc.types.Field(String, graphql_name='order_id')

    is_master = sgqlc.types.Field(Boolean, graphql_name='is_master')



class Mutation(sgqlc.types.Type):
    __schema__ = shiphero_schema
    __field_names__ = ('node', 'bill_create', 'bill_delete', 'bill_recalculate', 'bill_update', 'bill_submit', 'inventory_add', 'inventory_remove', 'inventory_subtract', 'inventory_replace', 'location_create', 'location_update', 'inventory_sync', 'inventory_sync_abort', 'inventory_generate_snapshot', 'inventory_abort_snapshot', 'lot_create', 'lot_update', 'lots_update', 'lot_delete', 'lot_assign_to_location', 'order_create', 'order_change_warehouse', 'order_cancel', 'order_update_fulfillment_status', 'order_add_line_items', 'order_remove_line_items', 'order_update_line_items', 'order_update_tags', 'order_add_tags', 'order_clear_tags', 'order_add_history_entry', 'order_update', 'order_update_holds', 'product_create', 'product_add_to_warehouse', 'product_delete', 'warehouse_product_delete', 'product_update', 'warehouse_product_update', 'kit_build', 'kit_clear', 'kit_remove_components', 'purchase_order_create', 'purchase_order_update', 'purchase_order_close', 'purchase_order_cancel', 'purchase_order_set_fulfillment_status', 'purchase_order_add_attachment', 'return_create', 'return_create_exchange', 'return_update_status', 'shipment_create', 'shipment_create_shipping_label', 'shipping_plan_create', 'vendor_create', 'vendor_delete', 'vendor_add_product', 'vendor_remove_product', 'webhook_create', 'webhook_delete')
    node = sgqlc.types.Field('Node', graphql_name='node', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='id', default=None)),
))
    )
    '''Arguments:

    * `id` (`ID!`)
    '''

    bill_create = sgqlc.types.Field(CreateBillOutput, graphql_name='bill_create', args=sgqlc.types.ArgDict((
        ('data', sgqlc.types.Arg(sgqlc.types.non_null(CreateBillInput), graphql_name='data', default=None)),
))
    )
    '''Arguments:

    * `data` (`CreateBillInput!`)
    '''

    bill_delete = sgqlc.types.Field('MutationOutput', graphql_name='bill_delete', args=sgqlc.types.ArgDict((
        ('data', sgqlc.types.Arg(sgqlc.types.non_null(DeleteBillInput), graphql_name='data', default=None)),
))
    )
    '''Arguments:

    * `data` (`DeleteBillInput!`)
    '''

    bill_recalculate = sgqlc.types.Field('RecalculateBillOutput', graphql_name='bill_recalculate', args=sgqlc.types.ArgDict((
        ('data', sgqlc.types.Arg(sgqlc.types.non_null(RecalculateBillInput), graphql_name='data', default=None)),
))
    )
    '''Arguments:

    * `data` (`RecalculateBillInput!`)
    '''

    bill_update = sgqlc.types.Field('MutationOutput', graphql_name='bill_update', args=sgqlc.types.ArgDict((
        ('data', sgqlc.types.Arg(sgqlc.types.non_null(UpdateBillInput), graphql_name='data', default=None)),
))
    )
    '''Arguments:

    * `data` (`UpdateBillInput!`)
    '''

    bill_submit = sgqlc.types.Field('MutationOutput', graphql_name='bill_submit', args=sgqlc.types.ArgDict((
        ('data', sgqlc.types.Arg(sgqlc.types.non_null(SubmitBillInput), graphql_name='data', default=None)),
))
    )
    '''Arguments:

    * `data` (`SubmitBillInput!`)
    '''

    inventory_add = sgqlc.types.Field('UpdateInventoryOutput', graphql_name='inventory_add', args=sgqlc.types.ArgDict((
        ('data', sgqlc.types.Arg(sgqlc.types.non_null(UpdateInventoryInput), graphql_name='data', default=None)),
))
    )
    '''Arguments:

    * `data` (`UpdateInventoryInput!`)
    '''

    inventory_remove = sgqlc.types.Field('UpdateInventoryOutput', graphql_name='inventory_remove', args=sgqlc.types.ArgDict((
        ('data', sgqlc.types.Arg(sgqlc.types.non_null(UpdateInventoryInput), graphql_name='data', default=None)),
))
    )
    '''Arguments:

    * `data` (`UpdateInventoryInput!`)
    '''

    inventory_subtract = sgqlc.types.Field('UpdateInventoryOutput', graphql_name='inventory_subtract', args=sgqlc.types.ArgDict((
        ('data', sgqlc.types.Arg(sgqlc.types.non_null(UpdateInventoryInput), graphql_name='data', default=None)),
))
    )
    '''Arguments:

    * `data` (`UpdateInventoryInput!`)
    '''

    inventory_replace = sgqlc.types.Field('UpdateInventoryOutput', graphql_name='inventory_replace', args=sgqlc.types.ArgDict((
        ('data', sgqlc.types.Arg(sgqlc.types.non_null(ReplaceInventoryInput), graphql_name='data', default=None)),
))
    )
    '''Arguments:

    * `data` (`ReplaceInventoryInput!`)
    '''

    location_create = sgqlc.types.Field(LocationOutput, graphql_name='location_create', args=sgqlc.types.ArgDict((
        ('data', sgqlc.types.Arg(sgqlc.types.non_null(CreateLocationInput), graphql_name='data', default=None)),
))
    )
    '''Arguments:

    * `data` (`CreateLocationInput!`)
    '''

    location_update = sgqlc.types.Field(LocationOutput, graphql_name='location_update', args=sgqlc.types.ArgDict((
        ('data', sgqlc.types.Arg(sgqlc.types.non_null(UpdateLocationInput), graphql_name='data', default=None)),
))
    )
    '''Arguments:

    * `data` (`UpdateLocationInput!`)
    '''

    inventory_sync = sgqlc.types.Field(InventorySyncOutput, graphql_name='inventory_sync', args=sgqlc.types.ArgDict((
        ('data', sgqlc.types.Arg(sgqlc.types.non_null(InventorySyncInput), graphql_name='data', default=None)),
))
    )
    '''Arguments:

    * `data` (`InventorySyncInput!`)
    '''

    inventory_sync_abort = sgqlc.types.Field(AbortInventorySyncOutput, graphql_name='inventory_sync_abort', args=sgqlc.types.ArgDict((
        ('data', sgqlc.types.Arg(sgqlc.types.non_null(AbortInventorySyncInput), graphql_name='data', default=None)),
))
    )
    '''Arguments:

    * `data` (`AbortInventorySyncInput!`)
    '''

    inventory_generate_snapshot = sgqlc.types.Field(InventorySnapshotOutput, graphql_name='inventory_generate_snapshot', args=sgqlc.types.ArgDict((
        ('data', sgqlc.types.Arg(sgqlc.types.non_null(InventoryGenerateSnapshotInput), graphql_name='data', default=None)),
))
    )
    '''Arguments:

    * `data` (`InventoryGenerateSnapshotInput!`)
    '''

    inventory_abort_snapshot = sgqlc.types.Field(InventorySnapshotOutput, graphql_name='inventory_abort_snapshot', args=sgqlc.types.ArgDict((
        ('data', sgqlc.types.Arg(sgqlc.types.non_null(InventoryAbortSnapshotInput), graphql_name='data', default=None)),
))
    )
    '''Arguments:

    * `data` (`InventoryAbortSnapshotInput!`)
    '''

    lot_create = sgqlc.types.Field(CreateLotOutput, graphql_name='lot_create', args=sgqlc.types.ArgDict((
        ('data', sgqlc.types.Arg(sgqlc.types.non_null(CreateLotInput), graphql_name='data', default=None)),
))
    )
    '''Arguments:

    * `data` (`CreateLotInput!`)
    '''

    lot_update = sgqlc.types.Field('UpdateLotOutput', graphql_name='lot_update', args=sgqlc.types.ArgDict((
        ('data', sgqlc.types.Arg(sgqlc.types.non_null(UpdateLotInput), graphql_name='data', default=None)),
))
    )
    '''Arguments:

    * `data` (`UpdateLotInput!`)
    '''

    lots_update = sgqlc.types.Field('UpdateLotsOutput', graphql_name='lots_update', args=sgqlc.types.ArgDict((
        ('data', sgqlc.types.Arg(sgqlc.types.non_null(UpdateLotsInput), graphql_name='data', default=None)),
))
    )
    '''Arguments:

    * `data` (`UpdateLotsInput!`)
    '''

    lot_delete = sgqlc.types.Field(DeleteLotOutput, graphql_name='lot_delete', args=sgqlc.types.ArgDict((
        ('data', sgqlc.types.Arg(sgqlc.types.non_null(DeleteLotInput), graphql_name='data', default=None)),
))
    )
    '''Arguments:

    * `data` (`DeleteLotInput!`)
    '''

    lot_assign_to_location = sgqlc.types.Field(AssignLotToLocationOutput, graphql_name='lot_assign_to_location', args=sgqlc.types.ArgDict((
        ('data', sgqlc.types.Arg(sgqlc.types.non_null(AssignLotToLocationInput), graphql_name='data', default=None)),
))
    )
    '''Arguments:

    * `data` (`AssignLotToLocationInput!`)
    '''

    order_create = sgqlc.types.Field('OrderMutationOutput', graphql_name='order_create', args=sgqlc.types.ArgDict((
        ('data', sgqlc.types.Arg(sgqlc.types.non_null(CreateOrderInput), graphql_name='data', default=None)),
))
    )
    '''Arguments:

    * `data` (`CreateOrderInput!`)
    '''

    order_change_warehouse = sgqlc.types.Field('OrderMutationOutput', graphql_name='order_change_warehouse', args=sgqlc.types.ArgDict((
        ('data', sgqlc.types.Arg(sgqlc.types.non_null(ChangeOrderWarehouseInput), graphql_name='data', default=None)),
))
    )
    '''Arguments:

    * `data` (`ChangeOrderWarehouseInput!`)
    '''

    order_cancel = sgqlc.types.Field('OrderMutationOutput', graphql_name='order_cancel', args=sgqlc.types.ArgDict((
        ('data', sgqlc.types.Arg(sgqlc.types.non_null(CancelOrderInput), graphql_name='data', default=None)),
))
    )
    '''Arguments:

    * `data` (`CancelOrderInput!`)
    '''

    order_update_fulfillment_status = sgqlc.types.Field('OrderMutationOutput', graphql_name='order_update_fulfillment_status', args=sgqlc.types.ArgDict((
        ('data', sgqlc.types.Arg(sgqlc.types.non_null(UpdateOrderFulfillmentStatusInput), graphql_name='data', default=None)),
))
    )
    '''Arguments:

    * `data` (`UpdateOrderFulfillmentStatusInput!`)
    '''

    order_add_line_items = sgqlc.types.Field('OrderMutationOutput', graphql_name='order_add_line_items', args=sgqlc.types.ArgDict((
        ('data', sgqlc.types.Arg(sgqlc.types.non_null(AddLineItemsInput), graphql_name='data', default=None)),
))
    )
    '''Arguments:

    * `data` (`AddLineItemsInput!`)
    '''

    order_remove_line_items = sgqlc.types.Field('OrderMutationOutput', graphql_name='order_remove_line_items', args=sgqlc.types.ArgDict((
        ('data', sgqlc.types.Arg(sgqlc.types.non_null(RemoveLineItemsInput), graphql_name='data', default=None)),
))
    )
    '''Arguments:

    * `data` (`RemoveLineItemsInput!`)
    '''

    order_update_line_items = sgqlc.types.Field('OrderMutationOutput', graphql_name='order_update_line_items', args=sgqlc.types.ArgDict((
        ('data', sgqlc.types.Arg(sgqlc.types.non_null(UpdateLineItemsInput), graphql_name='data', default=None)),
))
    )
    '''Arguments:

    * `data` (`UpdateLineItemsInput!`)
    '''

    order_update_tags = sgqlc.types.Field('OrderMutationOutput', graphql_name='order_update_tags', args=sgqlc.types.ArgDict((
        ('data', sgqlc.types.Arg(sgqlc.types.non_null(UpdateTagsInput), graphql_name='data', default=None)),
))
    )
    '''Arguments:

    * `data` (`UpdateTagsInput!`)
    '''

    order_add_tags = sgqlc.types.Field('OrderMutationOutput', graphql_name='order_add_tags', args=sgqlc.types.ArgDict((
        ('data', sgqlc.types.Arg(sgqlc.types.non_null(UpdateTagsInput), graphql_name='data', default=None)),
))
    )
    '''Arguments:

    * `data` (`UpdateTagsInput!`)
    '''

    order_clear_tags = sgqlc.types.Field('OrderMutationOutput', graphql_name='order_clear_tags', args=sgqlc.types.ArgDict((
        ('data', sgqlc.types.Arg(sgqlc.types.non_null(UpdateOrderInputBase), graphql_name='data', default=None)),
))
    )
    '''Arguments:

    * `data` (`UpdateOrderInputBase!`)
    '''

    order_add_history_entry = sgqlc.types.Field('OrderMutationOutput', graphql_name='order_add_history_entry', args=sgqlc.types.ArgDict((
        ('data', sgqlc.types.Arg(sgqlc.types.non_null(AddHistoryInput), graphql_name='data', default=None)),
))
    )
    '''Arguments:

    * `data` (`AddHistoryInput!`)
    '''

    order_update = sgqlc.types.Field('OrderMutationOutput', graphql_name='order_update', args=sgqlc.types.ArgDict((
        ('data', sgqlc.types.Arg(sgqlc.types.non_null(UpdateOrderInput), graphql_name='data', default=None)),
))
    )
    '''Arguments:

    * `data` (`UpdateOrderInput!`)
    '''

    order_update_holds = sgqlc.types.Field('OrderMutationOutput', graphql_name='order_update_holds', args=sgqlc.types.ArgDict((
        ('data', sgqlc.types.Arg(sgqlc.types.non_null(UpdateOrderHoldsInput), graphql_name='data', default=None)),
))
    )
    '''Arguments:

    * `data` (`UpdateOrderHoldsInput!`)
    '''

    product_create = sgqlc.types.Field(CreateProductOutput, graphql_name='product_create', args=sgqlc.types.ArgDict((
        ('data', sgqlc.types.Arg(sgqlc.types.non_null(CreateProductInput), graphql_name='data', default=None)),
))
    )
    '''Arguments:

    * `data` (`CreateProductInput!`)
    '''

    product_add_to_warehouse = sgqlc.types.Field('WarehouseProductMutationOutput', graphql_name='product_add_to_warehouse', args=sgqlc.types.ArgDict((
        ('data', sgqlc.types.Arg(sgqlc.types.non_null(AddProductToWarehouseInput), graphql_name='data', default=None)),
))
    )
    '''Arguments:

    * `data` (`AddProductToWarehouseInput!`)
    '''

    product_delete = sgqlc.types.Field('MutationOutput', graphql_name='product_delete', args=sgqlc.types.ArgDict((
        ('data', sgqlc.types.Arg(sgqlc.types.non_null(DeleteProductInput), graphql_name='data', default=None)),
))
    )
    '''Arguments:

    * `data` (`DeleteProductInput!`)
    '''

    warehouse_product_delete = sgqlc.types.Field('MutationOutput', graphql_name='warehouse_product_delete', args=sgqlc.types.ArgDict((
        ('data', sgqlc.types.Arg(sgqlc.types.non_null(DeleteWarehouseProductInput), graphql_name='data', default=None)),
))
    )
    '''Arguments:

    * `data` (`DeleteWarehouseProductInput!`)
    '''

    product_update = sgqlc.types.Field('ProductMutationOutput', graphql_name='product_update', args=sgqlc.types.ArgDict((
        ('data', sgqlc.types.Arg(sgqlc.types.non_null(UpdateProductInput), graphql_name='data', default=None)),
))
    )
    '''Arguments:

    * `data` (`UpdateProductInput!`)
    '''

    warehouse_product_update = sgqlc.types.Field('WarehouseProductMutationOutput', graphql_name='warehouse_product_update', args=sgqlc.types.ArgDict((
        ('data', sgqlc.types.Arg(sgqlc.types.non_null(UpdateWarehouseProductInput), graphql_name='data', default=None)),
))
    )
    '''Arguments:

    * `data` (`UpdateWarehouseProductInput!`)
    '''

    kit_build = sgqlc.types.Field('ProductMutationOutput', graphql_name='kit_build', args=sgqlc.types.ArgDict((
        ('data', sgqlc.types.Arg(sgqlc.types.non_null(BuildKitInput), graphql_name='data', default=None)),
))
    )
    '''Arguments:

    * `data` (`BuildKitInput!`)
    '''

    kit_clear = sgqlc.types.Field('MutationOutput', graphql_name='kit_clear', args=sgqlc.types.ArgDict((
        ('data', sgqlc.types.Arg(sgqlc.types.non_null(ClearKitInput), graphql_name='data', default=None)),
))
    )
    '''Arguments:

    * `data` (`ClearKitInput!`)
    '''

    kit_remove_components = sgqlc.types.Field('ProductMutationOutput', graphql_name='kit_remove_components', args=sgqlc.types.ArgDict((
        ('data', sgqlc.types.Arg(sgqlc.types.non_null(RemoveKitComponentsInput), graphql_name='data', default=None)),
))
    )
    '''Arguments:

    * `data` (`RemoveKitComponentsInput!`)
    '''

    purchase_order_create = sgqlc.types.Field(CreatePurchaseOrderOutput, graphql_name='purchase_order_create', args=sgqlc.types.ArgDict((
        ('data', sgqlc.types.Arg(sgqlc.types.non_null(CreatePurchaseOrderInput), graphql_name='data', default=None)),
))
    )
    '''Arguments:

    * `data` (`CreatePurchaseOrderInput!`)
    '''

    purchase_order_update = sgqlc.types.Field('UpdatePurchaseOrderOutput', graphql_name='purchase_order_update', args=sgqlc.types.ArgDict((
        ('data', sgqlc.types.Arg(sgqlc.types.non_null(UpdatePurchaseOrderInput), graphql_name='data', default=None)),
))
    )
    '''Arguments:

    * `data` (`UpdatePurchaseOrderInput!`)
    '''

    purchase_order_close = sgqlc.types.Field(ClosePurchaseOrderOutput, graphql_name='purchase_order_close', args=sgqlc.types.ArgDict((
        ('data', sgqlc.types.Arg(sgqlc.types.non_null(ClosePurchaseOrderInput), graphql_name='data', default=None)),
))
    )
    '''Arguments:

    * `data` (`ClosePurchaseOrderInput!`)
    '''

    purchase_order_cancel = sgqlc.types.Field(CancelPurchaseOrderOutput, graphql_name='purchase_order_cancel', args=sgqlc.types.ArgDict((
        ('data', sgqlc.types.Arg(sgqlc.types.non_null(CancelPurchaseOrderInput), graphql_name='data', default=None)),
))
    )
    '''Arguments:

    * `data` (`CancelPurchaseOrderInput!`)
    '''

    purchase_order_set_fulfillment_status = sgqlc.types.Field('SetPurchaseOrderFulfillmentStatusOutput', graphql_name='purchase_order_set_fulfillment_status', args=sgqlc.types.ArgDict((
        ('data', sgqlc.types.Arg(sgqlc.types.non_null(SetPurchaseOrderFulfillmentStatusInput), graphql_name='data', default=None)),
))
    )
    '''Arguments:

    * `data` (`SetPurchaseOrderFulfillmentStatusInput!`)
    '''

    purchase_order_add_attachment = sgqlc.types.Field(AddPurchaseOrderAttachmentOutput, graphql_name='purchase_order_add_attachment', args=sgqlc.types.ArgDict((
        ('data', sgqlc.types.Arg(sgqlc.types.non_null(AddPurchaseOrderAttachmentInput), graphql_name='data', default=None)),
))
    )
    '''Arguments:

    * `data` (`AddPurchaseOrderAttachmentInput!`)
    '''

    return_create = sgqlc.types.Field(CreateReturnOutput, graphql_name='return_create', args=sgqlc.types.ArgDict((
        ('data', sgqlc.types.Arg(sgqlc.types.non_null(CreateReturnInput), graphql_name='data', default=None)),
))
    )
    '''Arguments:

    * `data` (`CreateReturnInput!`)
    '''

    return_create_exchange = sgqlc.types.Field(CreateReturnExchangeOutput, graphql_name='return_create_exchange', args=sgqlc.types.ArgDict((
        ('data', sgqlc.types.Arg(sgqlc.types.non_null(CreateReturnExchangeInput), graphql_name='data', default=None)),
))
    )
    '''Arguments:

    * `data` (`CreateReturnExchangeInput!`)
    '''

    return_update_status = sgqlc.types.Field('UpdateReturnStatusOutput', graphql_name='return_update_status', args=sgqlc.types.ArgDict((
        ('data', sgqlc.types.Arg(sgqlc.types.non_null(UpdateReturnStatusInput), graphql_name='data', default=None)),
))
    )
    '''Arguments:

    * `data` (`UpdateReturnStatusInput!`)
    '''

    shipment_create = sgqlc.types.Field(CreateShipmentOutput, graphql_name='shipment_create', args=sgqlc.types.ArgDict((
        ('data', sgqlc.types.Arg(sgqlc.types.non_null(CreateShipmentInput), graphql_name='data', default=None)),
))
    )
    '''Arguments:

    * `data` (`CreateShipmentInput!`)
    '''

    shipment_create_shipping_label = sgqlc.types.Field(CreateShippingLabelOutput, graphql_name='shipment_create_shipping_label', args=sgqlc.types.ArgDict((
        ('data', sgqlc.types.Arg(sgqlc.types.non_null(CreateShippingLabelInput), graphql_name='data', default=None)),
))
    )
    '''Arguments:

    * `data` (`CreateShippingLabelInput!`)
    '''

    shipping_plan_create = sgqlc.types.Field(CreateShippingPlanOutput, graphql_name='shipping_plan_create', args=sgqlc.types.ArgDict((
        ('data', sgqlc.types.Arg(sgqlc.types.non_null(CreateShippingPlanInput), graphql_name='data', default=None)),
))
    )
    '''Arguments:

    * `data` (`CreateShippingPlanInput!`)
    '''

    vendor_create = sgqlc.types.Field(CreateVendorOutput, graphql_name='vendor_create', args=sgqlc.types.ArgDict((
        ('data', sgqlc.types.Arg(sgqlc.types.non_null(CreateVendorInput), graphql_name='data', default=None)),
))
    )
    '''Arguments:

    * `data` (`CreateVendorInput!`)
    '''

    vendor_delete = sgqlc.types.Field('MutationOutput', graphql_name='vendor_delete', args=sgqlc.types.ArgDict((
        ('data', sgqlc.types.Arg(sgqlc.types.non_null(DeleteVendorInput), graphql_name='data', default=None)),
))
    )
    '''Arguments:

    * `data` (`DeleteVendorInput!`)
    '''

    vendor_add_product = sgqlc.types.Field('MutationOutput', graphql_name='vendor_add_product', args=sgqlc.types.ArgDict((
        ('data', sgqlc.types.Arg(sgqlc.types.non_null(AddProductToVendorInput), graphql_name='data', default=None)),
))
    )
    '''Arguments:

    * `data` (`AddProductToVendorInput!`)
    '''

    vendor_remove_product = sgqlc.types.Field('MutationOutput', graphql_name='vendor_remove_product', args=sgqlc.types.ArgDict((
        ('data', sgqlc.types.Arg(sgqlc.types.non_null(RemoveProductFromVendorInput), graphql_name='data', default=None)),
))
    )
    '''Arguments:

    * `data` (`RemoveProductFromVendorInput!`)
    '''

    webhook_create = sgqlc.types.Field(CreateWebhookOutput, graphql_name='webhook_create', args=sgqlc.types.ArgDict((
        ('data', sgqlc.types.Arg(sgqlc.types.non_null(CreateWebhookInput), graphql_name='data', default=None)),
))
    )
    '''Arguments:

    * `data` (`CreateWebhookInput!`)
    '''

    webhook_delete = sgqlc.types.Field('MutationOutput', graphql_name='webhook_delete', args=sgqlc.types.ArgDict((
        ('data', sgqlc.types.Arg(sgqlc.types.non_null(DeleteWebhookInput), graphql_name='data', default=None)),
))
    )
    '''Arguments:

    * `data` (`DeleteWebhookInput!`)
    '''



class MutationOutput(sgqlc.types.Type):
    __schema__ = shiphero_schema
    __field_names__ = ('request_id', 'complexity')
    request_id = sgqlc.types.Field(String, graphql_name='request_id')

    complexity = sgqlc.types.Field(Int, graphql_name='complexity')



class Node(sgqlc.types.Interface):
    __schema__ = shiphero_schema
    __field_names__ = ('id',)
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')



class Order(sgqlc.types.Type):
    __schema__ = shiphero_schema
    __field_names__ = ('id', 'legacy_id', 'order_number', 'partner_order_id', 'shop_name', 'fulfillment_status', 'order_date', 'total_tax', 'subtotal', 'total_discounts', 'total_price', 'box_name', 'auto_print_return_label', 'custom_invoice_url', 'account_id', 'email', 'profile', 'gift_note', 'packing_note', 'required_ship_date', 'shipping_lines', 'shipping_address', 'billing_address', 'tags', 'line_items', 'authorizations', 'holds', 'shipments', 'returns', 'rma_labels', 'flagged', 'saturday_delivery', 'ignore_address_validation_errors', 'skip_address_validation', 'priority_flag', 'allocation_priority', 'allocations', 'source', 'third_party_shipper', 'gift_invoice', 'allow_partial', 'require_signature', 'adult_signature_required', 'alcohol', 'expected_weight_in_oz', 'insurance', 'insurance_amount', 'currency', 'has_dry_ice', 'allow_split', 'hold_until_date', 'incoterms', 'tax_id', 'tax_type', 'dry_ice_weight_in_lbs', 'ftr_exemption', 'address_is_business', 'order_history', 'merged_orders')
    id = sgqlc.types.Field(String, graphql_name='id')

    legacy_id = sgqlc.types.Field(Int, graphql_name='legacy_id')

    order_number = sgqlc.types.Field(String, graphql_name='order_number')

    partner_order_id = sgqlc.types.Field(String, graphql_name='partner_order_id')

    shop_name = sgqlc.types.Field(String, graphql_name='shop_name')

    fulfillment_status = sgqlc.types.Field(String, graphql_name='fulfillment_status')

    order_date = sgqlc.types.Field(ISODateTime, graphql_name='order_date')

    total_tax = sgqlc.types.Field(String, graphql_name='total_tax')

    subtotal = sgqlc.types.Field(String, graphql_name='subtotal')

    total_discounts = sgqlc.types.Field(String, graphql_name='total_discounts')

    total_price = sgqlc.types.Field(String, graphql_name='total_price')

    box_name = sgqlc.types.Field(String, graphql_name='box_name')

    auto_print_return_label = sgqlc.types.Field(Boolean, graphql_name='auto_print_return_label')

    custom_invoice_url = sgqlc.types.Field(String, graphql_name='custom_invoice_url')

    account_id = sgqlc.types.Field(String, graphql_name='account_id')

    email = sgqlc.types.Field(String, graphql_name='email')

    profile = sgqlc.types.Field(String, graphql_name='profile')

    gift_note = sgqlc.types.Field(String, graphql_name='gift_note')

    packing_note = sgqlc.types.Field(String, graphql_name='packing_note')

    required_ship_date = sgqlc.types.Field(ISODateTime, graphql_name='required_ship_date')

    shipping_lines = sgqlc.types.Field('ShippingLines', graphql_name='shipping_lines')

    shipping_address = sgqlc.types.Field('OrderAddress', graphql_name='shipping_address')

    billing_address = sgqlc.types.Field('OrderAddress', graphql_name='billing_address')

    tags = sgqlc.types.Field(sgqlc.types.list_of(String), graphql_name='tags')

    line_items = sgqlc.types.Field(LineItemConnection, graphql_name='line_items', args=sgqlc.types.ArgDict((
        ('sort', sgqlc.types.Arg(String, graphql_name='sort', default=None)),
        ('before', sgqlc.types.Arg(String, graphql_name='before', default=None)),
        ('after', sgqlc.types.Arg(String, graphql_name='after', default=None)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
))
    )
    '''Arguments:

    * `sort` (`String`)
    * `before` (`String`)
    * `after` (`String`)
    * `first` (`Int`)
    * `last` (`Int`)
    '''

    authorizations = sgqlc.types.Field(sgqlc.types.list_of(Authorization), graphql_name='authorizations')

    holds = sgqlc.types.Field('OrderHolds', graphql_name='holds')

    shipments = sgqlc.types.Field(sgqlc.types.list_of('Shipment'), graphql_name='shipments')

    returns = sgqlc.types.Field(sgqlc.types.list_of('Return'), graphql_name='returns')

    rma_labels = sgqlc.types.Field(sgqlc.types.list_of('RMALabel'), graphql_name='rma_labels')

    flagged = sgqlc.types.Field(Boolean, graphql_name='flagged')

    saturday_delivery = sgqlc.types.Field(Boolean, graphql_name='saturday_delivery')

    ignore_address_validation_errors = sgqlc.types.Field(Boolean, graphql_name='ignore_address_validation_errors')

    skip_address_validation = sgqlc.types.Field(Boolean, graphql_name='skip_address_validation')

    priority_flag = sgqlc.types.Field(Boolean, graphql_name='priority_flag')

    allocation_priority = sgqlc.types.Field(Int, graphql_name='allocation_priority')

    allocations = sgqlc.types.Field(sgqlc.types.list_of('OrderWarehouseAllocation'), graphql_name='allocations')

    source = sgqlc.types.Field(String, graphql_name='source')

    third_party_shipper = sgqlc.types.Field('OrderThirdPartyShipper', graphql_name='third_party_shipper')

    gift_invoice = sgqlc.types.Field(Boolean, graphql_name='gift_invoice')

    allow_partial = sgqlc.types.Field(Boolean, graphql_name='allow_partial')

    require_signature = sgqlc.types.Field(Boolean, graphql_name='require_signature')

    adult_signature_required = sgqlc.types.Field(Boolean, graphql_name='adult_signature_required')

    alcohol = sgqlc.types.Field(Boolean, graphql_name='alcohol')

    expected_weight_in_oz = sgqlc.types.Field(String, graphql_name='expected_weight_in_oz')

    insurance = sgqlc.types.Field(Boolean, graphql_name='insurance')

    insurance_amount = sgqlc.types.Field(String, graphql_name='insurance_amount')

    currency = sgqlc.types.Field(String, graphql_name='currency')

    has_dry_ice = sgqlc.types.Field(Boolean, graphql_name='has_dry_ice')

    allow_split = sgqlc.types.Field(Boolean, graphql_name='allow_split')

    hold_until_date = sgqlc.types.Field(ISODateTime, graphql_name='hold_until_date')

    incoterms = sgqlc.types.Field(String, graphql_name='incoterms')

    tax_id = sgqlc.types.Field(String, graphql_name='tax_id')

    tax_type = sgqlc.types.Field(String, graphql_name='tax_type')

    dry_ice_weight_in_lbs = sgqlc.types.Field(String, graphql_name='dry_ice_weight_in_lbs')

    ftr_exemption = sgqlc.types.Field(Decimal, graphql_name='ftr_exemption')

    address_is_business = sgqlc.types.Field(Boolean, graphql_name='address_is_business')

    order_history = sgqlc.types.Field(sgqlc.types.list_of('OrderHistory'), graphql_name='order_history')

    merged_orders = sgqlc.types.Field(sgqlc.types.list_of(MergedOrder), graphql_name='merged_orders')



class OrderAddress(sgqlc.types.Type):
    __schema__ = shiphero_schema
    __field_names__ = ('first_name', 'last_name', 'company', 'address1', 'address2', 'city', 'state', 'state_code', 'zip', 'country', 'country_code', 'email', 'phone')
    first_name = sgqlc.types.Field(String, graphql_name='first_name')

    last_name = sgqlc.types.Field(String, graphql_name='last_name')

    company = sgqlc.types.Field(String, graphql_name='company')

    address1 = sgqlc.types.Field(String, graphql_name='address1')

    address2 = sgqlc.types.Field(String, graphql_name='address2')

    city = sgqlc.types.Field(String, graphql_name='city')

    state = sgqlc.types.Field(String, graphql_name='state')

    state_code = sgqlc.types.Field(String, graphql_name='state_code')

    zip = sgqlc.types.Field(String, graphql_name='zip')

    country = sgqlc.types.Field(String, graphql_name='country')

    country_code = sgqlc.types.Field(String, graphql_name='country_code')

    email = sgqlc.types.Field(String, graphql_name='email')

    phone = sgqlc.types.Field(String, graphql_name='phone')



class OrderConnection(sgqlc.types.relay.Connection):
    __schema__ = shiphero_schema
    __field_names__ = ('page_info', 'edges')
    page_info = sgqlc.types.Field(sgqlc.types.non_null('PageInfo'), graphql_name='pageInfo')

    edges = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of('OrderEdge')), graphql_name='edges')



class OrderEdge(sgqlc.types.Type):
    __schema__ = shiphero_schema
    __field_names__ = ('node', 'cursor')
    node = sgqlc.types.Field(Order, graphql_name='node')

    cursor = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='cursor')



class OrderHistory(sgqlc.types.Type):
    __schema__ = shiphero_schema
    __field_names__ = ('id', 'legacy_id', 'order_id', 'user_id', 'account_id', 'username', 'order_number', 'information', 'created_at', 'order')
    id = sgqlc.types.Field(String, graphql_name='id')

    legacy_id = sgqlc.types.Field(Int, graphql_name='legacy_id')

    order_id = sgqlc.types.Field(String, graphql_name='order_id')

    user_id = sgqlc.types.Field(String, graphql_name='user_id')

    account_id = sgqlc.types.Field(String, graphql_name='account_id')

    username = sgqlc.types.Field(String, graphql_name='username')

    order_number = sgqlc.types.Field(String, graphql_name='order_number')

    information = sgqlc.types.Field(String, graphql_name='information')

    created_at = sgqlc.types.Field(ISODateTime, graphql_name='created_at')

    order = sgqlc.types.Field(Order, graphql_name='order')



class OrderHistoryConnection(sgqlc.types.relay.Connection):
    __schema__ = shiphero_schema
    __field_names__ = ('page_info', 'edges')
    page_info = sgqlc.types.Field(sgqlc.types.non_null('PageInfo'), graphql_name='pageInfo')

    edges = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of('OrderHistoryEdge')), graphql_name='edges')



class OrderHistoryEdge(sgqlc.types.Type):
    __schema__ = shiphero_schema
    __field_names__ = ('node', 'cursor')
    node = sgqlc.types.Field(OrderHistory, graphql_name='node')

    cursor = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='cursor')



class OrderHistoryQueryResult(sgqlc.types.Type):
    __schema__ = shiphero_schema
    __field_names__ = ('request_id', 'complexity', 'data')
    request_id = sgqlc.types.Field(String, graphql_name='request_id')

    complexity = sgqlc.types.Field(Int, graphql_name='complexity')

    data = sgqlc.types.Field(OrderHistoryConnection, graphql_name='data', args=sgqlc.types.ArgDict((
        ('sort', sgqlc.types.Arg(String, graphql_name='sort', default=None)),
        ('before', sgqlc.types.Arg(String, graphql_name='before', default=None)),
        ('after', sgqlc.types.Arg(String, graphql_name='after', default=None)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
))
    )
    '''Arguments:

    * `sort` (`String`)
    * `before` (`String`)
    * `after` (`String`)
    * `first` (`Int`)
    * `last` (`Int`)
    '''



class OrderHolds(sgqlc.types.Type):
    __schema__ = shiphero_schema
    __field_names__ = ('fraud_hold', 'address_hold', 'shipping_method_hold', 'operator_hold', 'payment_hold', 'client_hold')
    fraud_hold = sgqlc.types.Field(Boolean, graphql_name='fraud_hold')

    address_hold = sgqlc.types.Field(Boolean, graphql_name='address_hold')

    shipping_method_hold = sgqlc.types.Field(Boolean, graphql_name='shipping_method_hold')

    operator_hold = sgqlc.types.Field(Boolean, graphql_name='operator_hold')

    payment_hold = sgqlc.types.Field(Boolean, graphql_name='payment_hold')

    client_hold = sgqlc.types.Field(Boolean, graphql_name='client_hold')



class OrderLineItemAllocation(sgqlc.types.Type):
    __schema__ = shiphero_schema
    __field_names__ = ('order_id', 'warehouse_id', 'allocated_at', 'line_item_id', 'sku', 'quantity_allocated', 'is_kit_component', 'allocation_reference')
    order_id = sgqlc.types.Field(String, graphql_name='order_id')

    warehouse_id = sgqlc.types.Field(String, graphql_name='warehouse_id')

    allocated_at = sgqlc.types.Field(ISODateTime, graphql_name='allocated_at')

    line_item_id = sgqlc.types.Field(String, graphql_name='line_item_id')

    sku = sgqlc.types.Field(String, graphql_name='sku')

    quantity_allocated = sgqlc.types.Field(Int, graphql_name='quantity_allocated')

    is_kit_component = sgqlc.types.Field(Boolean, graphql_name='is_kit_component')

    allocation_reference = sgqlc.types.Field(String, graphql_name='allocation_reference')



class OrderMutationOutput(sgqlc.types.Type):
    __schema__ = shiphero_schema
    __field_names__ = ('request_id', 'complexity', 'order')
    request_id = sgqlc.types.Field(String, graphql_name='request_id')

    complexity = sgqlc.types.Field(Int, graphql_name='complexity')

    order = sgqlc.types.Field(Order, graphql_name='order')



class OrderQueryResult(sgqlc.types.Type):
    __schema__ = shiphero_schema
    __field_names__ = ('request_id', 'complexity', 'data')
    request_id = sgqlc.types.Field(String, graphql_name='request_id')

    complexity = sgqlc.types.Field(Int, graphql_name='complexity')

    data = sgqlc.types.Field(Order, graphql_name='data')



class OrderThirdPartyShipper(sgqlc.types.Type):
    __schema__ = shiphero_schema
    __field_names__ = ('account_number', 'zip', 'country')
    account_number = sgqlc.types.Field(String, graphql_name='account_number')

    zip = sgqlc.types.Field(String, graphql_name='zip')

    country = sgqlc.types.Field(String, graphql_name='country')



class OrderWarehouseAllocation(sgqlc.types.Type):
    __schema__ = shiphero_schema
    __field_names__ = ('order_id', 'warehouse_id', 'allocated_at', 'allocation_reference', 'line_items')
    order_id = sgqlc.types.Field(String, graphql_name='order_id')

    warehouse_id = sgqlc.types.Field(String, graphql_name='warehouse_id')

    allocated_at = sgqlc.types.Field(ISODateTime, graphql_name='allocated_at')

    allocation_reference = sgqlc.types.Field(String, graphql_name='allocation_reference')

    line_items = sgqlc.types.Field(sgqlc.types.list_of(OrderLineItemAllocation), graphql_name='line_items')



class OrdersQueryResult(sgqlc.types.Type):
    __schema__ = shiphero_schema
    __field_names__ = ('request_id', 'complexity', 'data')
    request_id = sgqlc.types.Field(String, graphql_name='request_id')

    complexity = sgqlc.types.Field(Int, graphql_name='complexity')

    data = sgqlc.types.Field(OrderConnection, graphql_name='data', args=sgqlc.types.ArgDict((
        ('sort', sgqlc.types.Arg(String, graphql_name='sort', default=None)),
        ('before', sgqlc.types.Arg(String, graphql_name='before', default=None)),
        ('after', sgqlc.types.Arg(String, graphql_name='after', default=None)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
))
    )
    '''Arguments:

    * `sort` (`String`)
    * `before` (`String`)
    * `after` (`String`)
    * `first` (`Int`)
    * `last` (`Int`)
    '''



class Package(sgqlc.types.Type):
    __schema__ = shiphero_schema
    __field_names__ = ('id', 'legacy_id', 'shipment_id', 'warehouse_id', 'order_id', 'order_number', 'user_id', 'user_first_name', 'user_last_name', 'total_items', 'unique_items', 'barcodes_scanned', 'created_at', 'shipment', 'order')
    id = sgqlc.types.Field(String, graphql_name='id')

    legacy_id = sgqlc.types.Field(Int, graphql_name='legacy_id')

    shipment_id = sgqlc.types.Field(String, graphql_name='shipment_id')

    warehouse_id = sgqlc.types.Field(String, graphql_name='warehouse_id')

    order_id = sgqlc.types.Field(String, graphql_name='order_id')

    order_number = sgqlc.types.Field(String, graphql_name='order_number')

    user_id = sgqlc.types.Field(String, graphql_name='user_id')

    user_first_name = sgqlc.types.Field(String, graphql_name='user_first_name')

    user_last_name = sgqlc.types.Field(String, graphql_name='user_last_name')

    total_items = sgqlc.types.Field(Int, graphql_name='total_items')

    unique_items = sgqlc.types.Field(Int, graphql_name='unique_items')

    barcodes_scanned = sgqlc.types.Field(Int, graphql_name='barcodes_scanned')

    created_at = sgqlc.types.Field(ISODateTime, graphql_name='created_at')

    shipment = sgqlc.types.Field('Shipment', graphql_name='shipment')

    order = sgqlc.types.Field(Order, graphql_name='order')



class PackageConnection(sgqlc.types.relay.Connection):
    __schema__ = shiphero_schema
    __field_names__ = ('page_info', 'edges')
    page_info = sgqlc.types.Field(sgqlc.types.non_null('PageInfo'), graphql_name='pageInfo')

    edges = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of('PackageEdge')), graphql_name='edges')



class PackageEdge(sgqlc.types.Type):
    __schema__ = shiphero_schema
    __field_names__ = ('node', 'cursor')
    node = sgqlc.types.Field(Package, graphql_name='node')

    cursor = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='cursor')



class PacksPerDayQueryResult(sgqlc.types.Type):
    __schema__ = shiphero_schema
    __field_names__ = ('request_id', 'complexity', 'data')
    request_id = sgqlc.types.Field(String, graphql_name='request_id')

    complexity = sgqlc.types.Field(Int, graphql_name='complexity')

    data = sgqlc.types.Field(PackageConnection, graphql_name='data', args=sgqlc.types.ArgDict((
        ('sort', sgqlc.types.Arg(String, graphql_name='sort', default=None)),
        ('before', sgqlc.types.Arg(String, graphql_name='before', default=None)),
        ('after', sgqlc.types.Arg(String, graphql_name='after', default=None)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
))
    )
    '''Arguments:

    * `sort` (`String`)
    * `before` (`String`)
    * `after` (`String`)
    * `first` (`Int`)
    * `last` (`Int`)
    '''



class PageInfo(sgqlc.types.Type):
    __schema__ = shiphero_schema
    __field_names__ = ('has_next_page', 'has_previous_page', 'start_cursor', 'end_cursor')
    has_next_page = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='hasNextPage')

    has_previous_page = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='hasPreviousPage')

    start_cursor = sgqlc.types.Field(String, graphql_name='startCursor')

    end_cursor = sgqlc.types.Field(String, graphql_name='endCursor')



class Pick(sgqlc.types.Type):
    __schema__ = shiphero_schema
    __field_names__ = ('id', 'legacy_id', 'user_id', 'tote_id', 'line_item_id', 'pending_shipment_line_item_id', 'location_id', 'warehouse_id', 'order_id', 'order_number', 'user_first_name', 'user_last_name', 'inventory_bin', 'sku', 'quantity', 'picked_quantity', 'pick_type', 'barcode_scanned', 'created_at', 'line_item', 'order')
    id = sgqlc.types.Field(String, graphql_name='id')

    legacy_id = sgqlc.types.Field(Int, graphql_name='legacy_id')

    user_id = sgqlc.types.Field(String, graphql_name='user_id')

    tote_id = sgqlc.types.Field(String, graphql_name='tote_id')

    line_item_id = sgqlc.types.Field(String, graphql_name='line_item_id')

    pending_shipment_line_item_id = sgqlc.types.Field(String, graphql_name='pending_shipment_line_item_id')

    location_id = sgqlc.types.Field(String, graphql_name='location_id')

    warehouse_id = sgqlc.types.Field(String, graphql_name='warehouse_id')

    order_id = sgqlc.types.Field(String, graphql_name='order_id')

    order_number = sgqlc.types.Field(String, graphql_name='order_number')

    user_first_name = sgqlc.types.Field(String, graphql_name='user_first_name')

    user_last_name = sgqlc.types.Field(String, graphql_name='user_last_name')

    inventory_bin = sgqlc.types.Field(String, graphql_name='inventory_bin')

    sku = sgqlc.types.Field(String, graphql_name='sku')

    quantity = sgqlc.types.Field(Int, graphql_name='quantity')

    picked_quantity = sgqlc.types.Field(Int, graphql_name='picked_quantity')

    pick_type = sgqlc.types.Field(String, graphql_name='pick_type')

    barcode_scanned = sgqlc.types.Field(String, graphql_name='barcode_scanned')

    created_at = sgqlc.types.Field(ISODateTime, graphql_name='created_at')

    line_item = sgqlc.types.Field(LineItem, graphql_name='line_item')

    order = sgqlc.types.Field(Order, graphql_name='order')



class PickConnection(sgqlc.types.relay.Connection):
    __schema__ = shiphero_schema
    __field_names__ = ('page_info', 'edges')
    page_info = sgqlc.types.Field(sgqlc.types.non_null(PageInfo), graphql_name='pageInfo')

    edges = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of('PickEdge')), graphql_name='edges')



class PickEdge(sgqlc.types.Type):
    __schema__ = shiphero_schema
    __field_names__ = ('node', 'cursor')
    node = sgqlc.types.Field(Pick, graphql_name='node')

    cursor = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='cursor')



class PicksPerDayQueryResult(sgqlc.types.Type):
    __schema__ = shiphero_schema
    __field_names__ = ('request_id', 'complexity', 'data')
    request_id = sgqlc.types.Field(String, graphql_name='request_id')

    complexity = sgqlc.types.Field(Int, graphql_name='complexity')

    data = sgqlc.types.Field(PickConnection, graphql_name='data', args=sgqlc.types.ArgDict((
        ('sort', sgqlc.types.Arg(String, graphql_name='sort', default=None)),
        ('before', sgqlc.types.Arg(String, graphql_name='before', default=None)),
        ('after', sgqlc.types.Arg(String, graphql_name='after', default=None)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
))
    )
    '''Arguments:

    * `sort` (`String`)
    * `before` (`String`)
    * `after` (`String`)
    * `first` (`Int`)
    * `last` (`Int`)
    '''



class Product(sgqlc.types.Type):
    __schema__ = shiphero_schema
    __field_names__ = ('id', 'legacy_id', 'account_id', 'name', 'sku', 'barcode', 'country_of_manufacture', 'dimensions', 'tariff_code', 'kit', 'kit_build', 'no_air', 'final_sale', 'customs_value', 'customs_description', 'not_owned', 'dropship', 'needs_serial_number', 'thumbnail', 'large_thumbnail', 'created_at', 'updated_at', 'product_note', 'virtual', 'ignore_on_invoice', 'ignore_on_customs', 'active', 'needs_lot_tracking', 'warehouse_products', 'images', 'tags', 'vendors', 'kit_components')
    id = sgqlc.types.Field(String, graphql_name='id')

    legacy_id = sgqlc.types.Field(Int, graphql_name='legacy_id')

    account_id = sgqlc.types.Field(String, graphql_name='account_id')

    name = sgqlc.types.Field(String, graphql_name='name')

    sku = sgqlc.types.Field(String, graphql_name='sku')

    barcode = sgqlc.types.Field(String, graphql_name='barcode')

    country_of_manufacture = sgqlc.types.Field(String, graphql_name='country_of_manufacture')

    dimensions = sgqlc.types.Field(Dimensions, graphql_name='dimensions')

    tariff_code = sgqlc.types.Field(String, graphql_name='tariff_code')

    kit = sgqlc.types.Field(Boolean, graphql_name='kit')

    kit_build = sgqlc.types.Field(Boolean, graphql_name='kit_build')

    no_air = sgqlc.types.Field(Boolean, graphql_name='no_air')

    final_sale = sgqlc.types.Field(Boolean, graphql_name='final_sale')

    customs_value = sgqlc.types.Field(String, graphql_name='customs_value')

    customs_description = sgqlc.types.Field(String, graphql_name='customs_description')

    not_owned = sgqlc.types.Field(Boolean, graphql_name='not_owned')

    dropship = sgqlc.types.Field(Boolean, graphql_name='dropship')

    needs_serial_number = sgqlc.types.Field(Boolean, graphql_name='needs_serial_number')

    thumbnail = sgqlc.types.Field(String, graphql_name='thumbnail')

    large_thumbnail = sgqlc.types.Field(String, graphql_name='large_thumbnail')

    created_at = sgqlc.types.Field(ISODateTime, graphql_name='created_at')

    updated_at = sgqlc.types.Field(ISODateTime, graphql_name='updated_at')

    product_note = sgqlc.types.Field(String, graphql_name='product_note')

    virtual = sgqlc.types.Field(Boolean, graphql_name='virtual')

    ignore_on_invoice = sgqlc.types.Field(Boolean, graphql_name='ignore_on_invoice')

    ignore_on_customs = sgqlc.types.Field(Boolean, graphql_name='ignore_on_customs')

    active = sgqlc.types.Field(Boolean, graphql_name='active')

    needs_lot_tracking = sgqlc.types.Field(Boolean, graphql_name='needs_lot_tracking')

    warehouse_products = sgqlc.types.Field(sgqlc.types.list_of('WarehouseProduct'), graphql_name='warehouse_products')

    images = sgqlc.types.Field(sgqlc.types.list_of('ProductImage'), graphql_name='images')

    tags = sgqlc.types.Field(sgqlc.types.list_of(String), graphql_name='tags')

    vendors = sgqlc.types.Field(sgqlc.types.list_of('ProductVendor'), graphql_name='vendors')

    kit_components = sgqlc.types.Field(sgqlc.types.list_of(KitComponent), graphql_name='kit_components')



class ProductConnection(sgqlc.types.relay.Connection):
    __schema__ = shiphero_schema
    __field_names__ = ('page_info', 'edges')
    page_info = sgqlc.types.Field(sgqlc.types.non_null(PageInfo), graphql_name='pageInfo')

    edges = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of('ProductEdge')), graphql_name='edges')



class ProductEdge(sgqlc.types.Type):
    __schema__ = shiphero_schema
    __field_names__ = ('node', 'cursor')
    node = sgqlc.types.Field(Product, graphql_name='node')

    cursor = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='cursor')



class ProductImage(sgqlc.types.Type):
    __schema__ = shiphero_schema
    __field_names__ = ('src', 'position')
    src = sgqlc.types.Field(String, graphql_name='src')

    position = sgqlc.types.Field(Int, graphql_name='position')



class ProductMutationOutput(sgqlc.types.Type):
    __schema__ = shiphero_schema
    __field_names__ = ('request_id', 'complexity', 'product')
    request_id = sgqlc.types.Field(String, graphql_name='request_id')

    complexity = sgqlc.types.Field(Int, graphql_name='complexity')

    product = sgqlc.types.Field(Product, graphql_name='product')



class ProductQueryResult(sgqlc.types.Type):
    __schema__ = shiphero_schema
    __field_names__ = ('request_id', 'complexity', 'data')
    request_id = sgqlc.types.Field(String, graphql_name='request_id')

    complexity = sgqlc.types.Field(Int, graphql_name='complexity')

    data = sgqlc.types.Field(Product, graphql_name='data')



class ProductVendor(sgqlc.types.Type):
    __schema__ = shiphero_schema
    __field_names__ = ('vendor_id', 'vendor_sku', 'price')
    vendor_id = sgqlc.types.Field(String, graphql_name='vendor_id')

    vendor_sku = sgqlc.types.Field(String, graphql_name='vendor_sku')

    price = sgqlc.types.Field(String, graphql_name='price')



class ProductsQueryResult(sgqlc.types.Type):
    __schema__ = shiphero_schema
    __field_names__ = ('request_id', 'complexity', 'data')
    request_id = sgqlc.types.Field(String, graphql_name='request_id')

    complexity = sgqlc.types.Field(Int, graphql_name='complexity')

    data = sgqlc.types.Field(ProductConnection, graphql_name='data', args=sgqlc.types.ArgDict((
        ('sort', sgqlc.types.Arg(String, graphql_name='sort', default=None)),
        ('before', sgqlc.types.Arg(String, graphql_name='before', default=None)),
        ('after', sgqlc.types.Arg(String, graphql_name='after', default=None)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
))
    )
    '''Arguments:

    * `sort` (`String`)
    * `before` (`String`)
    * `after` (`String`)
    * `first` (`Int`)
    * `last` (`Int`)
    '''



class PurchaseOrder(sgqlc.types.Type):
    __schema__ = shiphero_schema
    __field_names__ = ('id', 'legacy_id', 'po_number', 'account_id', 'warehouse_id', 'vendor_id', 'created_at', 'po_date', 'date_closed', 'arrived_at', 'packing_note', 'fulfillment_status', 'po_note', 'description', 'partner_order_number', 'subtotal', 'discount', 'total_price', 'tax', 'shipping_method', 'shipping_carrier', 'shipping_name', 'shipping_price', 'tracking_number', 'pdf', 'images', 'payment_method', 'payment_due_by', 'payment_note', 'locking', 'locked_by_user_id', 'line_items', 'attachments', 'vendor', 'warehouse', 'origin_of_shipment', 'tracking_numbers')
    id = sgqlc.types.Field(String, graphql_name='id')

    legacy_id = sgqlc.types.Field(Int, graphql_name='legacy_id')

    po_number = sgqlc.types.Field(String, graphql_name='po_number')

    account_id = sgqlc.types.Field(String, graphql_name='account_id')

    warehouse_id = sgqlc.types.Field(String, graphql_name='warehouse_id')

    vendor_id = sgqlc.types.Field(String, graphql_name='vendor_id')

    created_at = sgqlc.types.Field(ISODateTime, graphql_name='created_at')

    po_date = sgqlc.types.Field(ISODateTime, graphql_name='po_date')

    date_closed = sgqlc.types.Field(ISODateTime, graphql_name='date_closed')

    arrived_at = sgqlc.types.Field(ISODateTime, graphql_name='arrived_at')

    packing_note = sgqlc.types.Field(String, graphql_name='packing_note')

    fulfillment_status = sgqlc.types.Field(String, graphql_name='fulfillment_status')

    po_note = sgqlc.types.Field(String, graphql_name='po_note')

    description = sgqlc.types.Field(String, graphql_name='description')

    partner_order_number = sgqlc.types.Field(String, graphql_name='partner_order_number')

    subtotal = sgqlc.types.Field(String, graphql_name='subtotal')

    discount = sgqlc.types.Field(String, graphql_name='discount')

    total_price = sgqlc.types.Field(String, graphql_name='total_price')

    tax = sgqlc.types.Field(String, graphql_name='tax')

    shipping_method = sgqlc.types.Field(String, graphql_name='shipping_method')

    shipping_carrier = sgqlc.types.Field(String, graphql_name='shipping_carrier')

    shipping_name = sgqlc.types.Field(String, graphql_name='shipping_name')

    shipping_price = sgqlc.types.Field(String, graphql_name='shipping_price')

    tracking_number = sgqlc.types.Field(String, graphql_name='tracking_number')

    pdf = sgqlc.types.Field(String, graphql_name='pdf')

    images = sgqlc.types.Field(String, graphql_name='images')

    payment_method = sgqlc.types.Field(String, graphql_name='payment_method')

    payment_due_by = sgqlc.types.Field(String, graphql_name='payment_due_by')

    payment_note = sgqlc.types.Field(String, graphql_name='payment_note')

    locking = sgqlc.types.Field(String, graphql_name='locking')

    locked_by_user_id = sgqlc.types.Field(String, graphql_name='locked_by_user_id')

    line_items = sgqlc.types.Field('PurchaseOrderLineItemConnection', graphql_name='line_items', args=sgqlc.types.ArgDict((
        ('sort', sgqlc.types.Arg(String, graphql_name='sort', default=None)),
        ('before', sgqlc.types.Arg(String, graphql_name='before', default=None)),
        ('after', sgqlc.types.Arg(String, graphql_name='after', default=None)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
))
    )
    '''Arguments:

    * `sort` (`String`)
    * `before` (`String`)
    * `after` (`String`)
    * `first` (`Int`)
    * `last` (`Int`)
    '''

    attachments = sgqlc.types.Field('PurchaseOrderAttachmentConnection', graphql_name='attachments', args=sgqlc.types.ArgDict((
        ('sort', sgqlc.types.Arg(String, graphql_name='sort', default=None)),
        ('before', sgqlc.types.Arg(String, graphql_name='before', default=None)),
        ('after', sgqlc.types.Arg(String, graphql_name='after', default=None)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
))
    )
    '''Arguments:

    * `sort` (`String`)
    * `before` (`String`)
    * `after` (`String`)
    * `first` (`Int`)
    * `last` (`Int`)
    '''

    vendor = sgqlc.types.Field('Vendor', graphql_name='vendor')

    warehouse = sgqlc.types.Field('Warehouse', graphql_name='warehouse')

    origin_of_shipment = sgqlc.types.Field(String, graphql_name='origin_of_shipment')

    tracking_numbers = sgqlc.types.Field('PurchaseOrderTrackingNumberConnection', graphql_name='tracking_numbers', args=sgqlc.types.ArgDict((
        ('sort', sgqlc.types.Arg(String, graphql_name='sort', default=None)),
        ('before', sgqlc.types.Arg(String, graphql_name='before', default=None)),
        ('after', sgqlc.types.Arg(String, graphql_name='after', default=None)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
))
    )
    '''Arguments:

    * `sort` (`String`)
    * `before` (`String`)
    * `after` (`String`)
    * `first` (`Int`)
    * `last` (`Int`)
    '''



class PurchaseOrderAttachment(sgqlc.types.Type):
    __schema__ = shiphero_schema
    __field_names__ = ('id', 'legacy_id', 'user_id', 'account_id', 'description', 'filename', 'file_type', 'created_at', 'url')
    id = sgqlc.types.Field(String, graphql_name='id')

    legacy_id = sgqlc.types.Field(Int, graphql_name='legacy_id')

    user_id = sgqlc.types.Field(String, graphql_name='user_id')

    account_id = sgqlc.types.Field(String, graphql_name='account_id')

    description = sgqlc.types.Field(String, graphql_name='description')

    filename = sgqlc.types.Field(String, graphql_name='filename')

    file_type = sgqlc.types.Field(String, graphql_name='file_type')

    created_at = sgqlc.types.Field(ISODateTime, graphql_name='created_at')

    url = sgqlc.types.Field(String, graphql_name='url')



class PurchaseOrderAttachmentConnection(sgqlc.types.relay.Connection):
    __schema__ = shiphero_schema
    __field_names__ = ('page_info', 'edges')
    page_info = sgqlc.types.Field(sgqlc.types.non_null(PageInfo), graphql_name='pageInfo')

    edges = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of('PurchaseOrderAttachmentEdge')), graphql_name='edges')



class PurchaseOrderAttachmentEdge(sgqlc.types.Type):
    __schema__ = shiphero_schema
    __field_names__ = ('node', 'cursor')
    node = sgqlc.types.Field(PurchaseOrderAttachment, graphql_name='node')

    cursor = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='cursor')



class PurchaseOrderConnection(sgqlc.types.relay.Connection):
    __schema__ = shiphero_schema
    __field_names__ = ('page_info', 'edges')
    page_info = sgqlc.types.Field(sgqlc.types.non_null(PageInfo), graphql_name='pageInfo')

    edges = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of('PurchaseOrderEdge')), graphql_name='edges')



class PurchaseOrderEdge(sgqlc.types.Type):
    __schema__ = shiphero_schema
    __field_names__ = ('node', 'cursor')
    node = sgqlc.types.Field(PurchaseOrder, graphql_name='node')

    cursor = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='cursor')



class PurchaseOrderLineItem(sgqlc.types.Type):
    __schema__ = shiphero_schema
    __field_names__ = ('id', 'legacy_id', 'po_id', 'account_id', 'warehouse_id', 'vendor_id', 'po_number', 'sku', 'vendor_sku', 'product_id', 'variant_id', 'quantity', 'quantity_received', 'quantity_rejected', 'price', 'product_name', 'option_title', 'expected_weight_in_lbs', 'fulfillment_status', 'sell_ahead', 'note', 'partner_line_item_id', 'barcode', 'updated_at', 'created_at', 'vendor', 'product', 'expiration_lots')
    id = sgqlc.types.Field(String, graphql_name='id')

    legacy_id = sgqlc.types.Field(Int, graphql_name='legacy_id')

    po_id = sgqlc.types.Field(String, graphql_name='po_id')

    account_id = sgqlc.types.Field(String, graphql_name='account_id')

    warehouse_id = sgqlc.types.Field(String, graphql_name='warehouse_id')

    vendor_id = sgqlc.types.Field(String, graphql_name='vendor_id')

    po_number = sgqlc.types.Field(String, graphql_name='po_number')

    sku = sgqlc.types.Field(String, graphql_name='sku')

    vendor_sku = sgqlc.types.Field(String, graphql_name='vendor_sku')

    product_id = sgqlc.types.Field(String, graphql_name='product_id')

    variant_id = sgqlc.types.Field(Int, graphql_name='variant_id')

    quantity = sgqlc.types.Field(Int, graphql_name='quantity')

    quantity_received = sgqlc.types.Field(Int, graphql_name='quantity_received')

    quantity_rejected = sgqlc.types.Field(Int, graphql_name='quantity_rejected')

    price = sgqlc.types.Field(String, graphql_name='price')

    product_name = sgqlc.types.Field(String, graphql_name='product_name')

    option_title = sgqlc.types.Field(String, graphql_name='option_title')

    expected_weight_in_lbs = sgqlc.types.Field(String, graphql_name='expected_weight_in_lbs')

    fulfillment_status = sgqlc.types.Field(String, graphql_name='fulfillment_status')

    sell_ahead = sgqlc.types.Field(Int, graphql_name='sell_ahead')

    note = sgqlc.types.Field(String, graphql_name='note')

    partner_line_item_id = sgqlc.types.Field(String, graphql_name='partner_line_item_id')

    barcode = sgqlc.types.Field(String, graphql_name='barcode')

    updated_at = sgqlc.types.Field(ISODateTime, graphql_name='updated_at')

    created_at = sgqlc.types.Field(ISODateTime, graphql_name='created_at')

    vendor = sgqlc.types.Field('Vendor', graphql_name='vendor')

    product = sgqlc.types.Field('WarehouseProduct', graphql_name='product')

    expiration_lots = sgqlc.types.Field(LotConnection, graphql_name='expiration_lots', args=sgqlc.types.ArgDict((
        ('sort', sgqlc.types.Arg(String, graphql_name='sort', default=None)),
        ('before', sgqlc.types.Arg(String, graphql_name='before', default=None)),
        ('after', sgqlc.types.Arg(String, graphql_name='after', default=None)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
))
    )
    '''Arguments:

    * `sort` (`String`)
    * `before` (`String`)
    * `after` (`String`)
    * `first` (`Int`)
    * `last` (`Int`)
    '''



class PurchaseOrderLineItemConnection(sgqlc.types.relay.Connection):
    __schema__ = shiphero_schema
    __field_names__ = ('page_info', 'edges')
    page_info = sgqlc.types.Field(sgqlc.types.non_null(PageInfo), graphql_name='pageInfo')

    edges = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of('PurchaseOrderLineItemEdge')), graphql_name='edges')



class PurchaseOrderLineItemEdge(sgqlc.types.Type):
    __schema__ = shiphero_schema
    __field_names__ = ('node', 'cursor')
    node = sgqlc.types.Field(PurchaseOrderLineItem, graphql_name='node')

    cursor = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='cursor')



class PurchaseOrderQueryResult(sgqlc.types.Type):
    __schema__ = shiphero_schema
    __field_names__ = ('request_id', 'complexity', 'data')
    request_id = sgqlc.types.Field(String, graphql_name='request_id')

    complexity = sgqlc.types.Field(Int, graphql_name='complexity')

    data = sgqlc.types.Field(PurchaseOrder, graphql_name='data')



class PurchaseOrderTrackingNumber(sgqlc.types.Type):
    __schema__ = shiphero_schema
    __field_names__ = ('id', 'legacy_id', 'po_id', 'carrier_id', 'carrier_value', 'tracking_number')
    id = sgqlc.types.Field(String, graphql_name='id')

    legacy_id = sgqlc.types.Field(Int, graphql_name='legacy_id')

    po_id = sgqlc.types.Field(String, graphql_name='po_id')

    carrier_id = sgqlc.types.Field(String, graphql_name='carrier_id')

    carrier_value = sgqlc.types.Field(String, graphql_name='carrier_value')

    tracking_number = sgqlc.types.Field(String, graphql_name='tracking_number')



class PurchaseOrderTrackingNumberConnection(sgqlc.types.relay.Connection):
    __schema__ = shiphero_schema
    __field_names__ = ('page_info', 'edges')
    page_info = sgqlc.types.Field(sgqlc.types.non_null(PageInfo), graphql_name='pageInfo')

    edges = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of('PurchaseOrderTrackingNumberEdge')), graphql_name='edges')



class PurchaseOrderTrackingNumberEdge(sgqlc.types.Type):
    __schema__ = shiphero_schema
    __field_names__ = ('node', 'cursor')
    node = sgqlc.types.Field(PurchaseOrderTrackingNumber, graphql_name='node')

    cursor = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='cursor')



class PurchaseOrdersQueryResult(sgqlc.types.Type):
    __schema__ = shiphero_schema
    __field_names__ = ('request_id', 'complexity', 'data')
    request_id = sgqlc.types.Field(String, graphql_name='request_id')

    complexity = sgqlc.types.Field(Int, graphql_name='complexity')

    data = sgqlc.types.Field(PurchaseOrderConnection, graphql_name='data', args=sgqlc.types.ArgDict((
        ('sort', sgqlc.types.Arg(String, graphql_name='sort', default=None)),
        ('before', sgqlc.types.Arg(String, graphql_name='before', default=None)),
        ('after', sgqlc.types.Arg(String, graphql_name='after', default=None)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
))
    )
    '''Arguments:

    * `sort` (`String`)
    * `before` (`String`)
    * `after` (`String`)
    * `first` (`Int`)
    * `last` (`Int`)
    '''



class Query(sgqlc.types.Type):
    __schema__ = shiphero_schema
    __field_names__ = ('node', 'account', 'me', 'uuid', 'bill', 'bills', 'fulfillment_invoice', 'fulfillment_invoices', 'location', 'locations', 'inventory_changes', 'inventory_sync_status', 'inventory_sync_items_status', 'inventory_sync_statuses', 'inventory_snapshot', 'inventory_snapshots', 'expiration_lots', 'order', 'orders', 'order_history', 'packs_per_day', 'picks_per_day', 'product', 'products', 'warehouse_products', 'purchase_order', 'purchase_orders', 'return_', 'returns', 'return_exchange', 'shipment', 'shipments', 'shipping_plan', 'tote_history', 'user_quota', 'vendors', 'webhooks')
    node = sgqlc.types.Field(Node, graphql_name='node', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='id', default=None)),
))
    )
    '''Arguments:

    * `id` (`ID!`)
    '''

    account = sgqlc.types.Field(AccountQueryResult, graphql_name='account', args=sgqlc.types.ArgDict((
        ('analyze', sgqlc.types.Arg(Boolean, graphql_name='analyze', default=None)),
))
    )
    '''Arguments:

    * `analyze` (`Boolean`)
    '''

    me = sgqlc.types.Field(CurrentUserQueryResult, graphql_name='me', args=sgqlc.types.ArgDict((
        ('analyze', sgqlc.types.Arg(Boolean, graphql_name='analyze', default=None)),
))
    )
    '''Arguments:

    * `analyze` (`Boolean`)
    '''

    uuid = sgqlc.types.Field(LegacyIdQueryResult, graphql_name='uuid', args=sgqlc.types.ArgDict((
        ('legacy_id', sgqlc.types.Arg(sgqlc.types.non_null(Int), graphql_name='legacy_id', default=None)),
        ('entity', sgqlc.types.Arg(sgqlc.types.non_null(EntityType), graphql_name='entity', default=None)),
        ('analyze', sgqlc.types.Arg(Boolean, graphql_name='analyze', default=None)),
))
    )
    '''Arguments:

    * `legacy_id` (`Int!`)
    * `entity` (`EntityType!`)
    * `analyze` (`Boolean`)
    '''

    bill = sgqlc.types.Field(BillQueryResult, graphql_name='bill', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(String), graphql_name='id', default=None)),
        ('analyze', sgqlc.types.Arg(Boolean, graphql_name='analyze', default=None)),
))
    )
    '''Arguments:

    * `id` (`String!`)
    * `analyze` (`Boolean`)
    '''

    bills = sgqlc.types.Field(BillsQueryResult, graphql_name='bills', args=sgqlc.types.ArgDict((
        ('from_date', sgqlc.types.Arg(ISODateTime, graphql_name='from_date', default=None)),
        ('to_date', sgqlc.types.Arg(ISODateTime, graphql_name='to_date', default=None)),
        ('status', sgqlc.types.Arg(String, graphql_name='status', default=None)),
        ('analyze', sgqlc.types.Arg(Boolean, graphql_name='analyze', default=None)),
))
    )
    '''Arguments:

    * `from_date` (`ISODateTime`)
    * `to_date` (`ISODateTime`)
    * `status` (`String`)
    * `analyze` (`Boolean`)
    '''

    fulfillment_invoice = sgqlc.types.Field(FulfillmentInvoiceQueryResult, graphql_name='fulfillment_invoice', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(String, graphql_name='id', default=None)),
        ('analyze', sgqlc.types.Arg(Boolean, graphql_name='analyze', default=None)),
))
    )
    '''Arguments:

    * `id` (`String`)
    * `analyze` (`Boolean`)
    '''

    fulfillment_invoices = sgqlc.types.Field(FulfillmentInvoicesQueryResult, graphql_name='fulfillment_invoices', args=sgqlc.types.ArgDict((
        ('date_from', sgqlc.types.Arg(ISODateTime, graphql_name='date_from', default=None)),
        ('date_to', sgqlc.types.Arg(ISODateTime, graphql_name='date_to', default=None)),
        ('analyze', sgqlc.types.Arg(Boolean, graphql_name='analyze', default=None)),
))
    )
    '''Arguments:

    * `date_from` (`ISODateTime`)
    * `date_to` (`ISODateTime`)
    * `analyze` (`Boolean`)
    '''

    location = sgqlc.types.Field(LocationQueryResult, graphql_name='location', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(String, graphql_name='id', default=None)),
        ('name', sgqlc.types.Arg(String, graphql_name='name', default=None)),
        ('analyze', sgqlc.types.Arg(Boolean, graphql_name='analyze', default=None)),
))
    )
    '''Arguments:

    * `id` (`String`)
    * `name` (`String`)
    * `analyze` (`Boolean`)
    '''

    locations = sgqlc.types.Field(LocationsQueryResult, graphql_name='locations', args=sgqlc.types.ArgDict((
        ('warehouse_id', sgqlc.types.Arg(String, graphql_name='warehouse_id', default=None)),
        ('analyze', sgqlc.types.Arg(Boolean, graphql_name='analyze', default=None)),
))
    )
    '''Arguments:

    * `warehouse_id` (`String`)
    * `analyze` (`Boolean`)
    '''

    inventory_changes = sgqlc.types.Field(InventoryChangesQueryResult, graphql_name='inventory_changes', args=sgqlc.types.ArgDict((
        ('sku', sgqlc.types.Arg(String, graphql_name='sku', default=None)),
        ('warehouse_id', sgqlc.types.Arg(String, graphql_name='warehouse_id', default=None)),
        ('location_id', sgqlc.types.Arg(String, graphql_name='location_id', default=None)),
        ('location_name', sgqlc.types.Arg(String, graphql_name='location_name', default=None)),
        ('date_from', sgqlc.types.Arg(ISODateTime, graphql_name='date_from', default=None)),
        ('date_to', sgqlc.types.Arg(ISODateTime, graphql_name='date_to', default=None)),
        ('analyze', sgqlc.types.Arg(Boolean, graphql_name='analyze', default=None)),
))
    )
    '''Arguments:

    * `sku` (`String`)
    * `warehouse_id` (`String`)
    * `location_id` (`String`)
    * `location_name` (`String`)
    * `date_from` (`ISODateTime`)
    * `date_to` (`ISODateTime`)
    * `analyze` (`Boolean`)
    '''

    inventory_sync_status = sgqlc.types.Field(InventorySyncBatchQueryResult, graphql_name='inventory_sync_status', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(String, graphql_name='id', default=None)),
        ('analyze', sgqlc.types.Arg(Boolean, graphql_name='analyze', default=None)),
))
    )
    '''Arguments:

    * `id` (`String`)
    * `analyze` (`Boolean`)
    '''

    inventory_sync_items_status = sgqlc.types.Field(InventorySyncRowsQueryResult, graphql_name='inventory_sync_items_status', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(String), graphql_name='id', default=None)),
        ('status', sgqlc.types.Arg(String, graphql_name='status', default=None)),
        ('analyze', sgqlc.types.Arg(Boolean, graphql_name='analyze', default=None)),
))
    )
    '''Arguments:

    * `id` (`String!`)
    * `status` (`String`)
    * `analyze` (`Boolean`)
    '''

    inventory_sync_statuses = sgqlc.types.Field(InventorySyncBatchesQueryResult, graphql_name='inventory_sync_statuses', args=sgqlc.types.ArgDict((
        ('warehouse_id', sgqlc.types.Arg(String, graphql_name='warehouse_id', default=None)),
        ('customer_account_id', sgqlc.types.Arg(String, graphql_name='customer_account_id', default=None)),
        ('status', sgqlc.types.Arg(String, graphql_name='status', default=None)),
        ('analyze', sgqlc.types.Arg(Boolean, graphql_name='analyze', default=None)),
))
    )
    '''Arguments:

    * `warehouse_id` (`String`)
    * `customer_account_id` (`String`)
    * `status` (`String`)
    * `analyze` (`Boolean`)
    '''

    inventory_snapshot = sgqlc.types.Field(InventorySnapshotQueryResult, graphql_name='inventory_snapshot', args=sgqlc.types.ArgDict((
        ('snapshot_id', sgqlc.types.Arg(sgqlc.types.non_null(String), graphql_name='snapshot_id', default=None)),
        ('analyze', sgqlc.types.Arg(Boolean, graphql_name='analyze', default=None)),
))
    )
    '''Arguments:

    * `snapshot_id` (`String!`)
    * `analyze` (`Boolean`)
    '''

    inventory_snapshots = sgqlc.types.Field(InventorySnapshotsQueryResult, graphql_name='inventory_snapshots', args=sgqlc.types.ArgDict((
        ('warehouse_id', sgqlc.types.Arg(String, graphql_name='warehouse_id', default=None)),
        ('customer_account_id', sgqlc.types.Arg(String, graphql_name='customer_account_id', default=None)),
        ('status', sgqlc.types.Arg(String, graphql_name='status', default=None)),
        ('analyze', sgqlc.types.Arg(Boolean, graphql_name='analyze', default=None)),
))
    )
    '''Arguments:

    * `warehouse_id` (`String`)
    * `customer_account_id` (`String`)
    * `status` (`String`)
    * `analyze` (`Boolean`)
    '''

    expiration_lots = sgqlc.types.Field(LotsQueryResult, graphql_name='expiration_lots', args=sgqlc.types.ArgDict((
        ('sku', sgqlc.types.Arg(String, graphql_name='sku', default=None)),
        ('po_id', sgqlc.types.Arg(String, graphql_name='po_id', default=None)),
        ('analyze', sgqlc.types.Arg(Boolean, graphql_name='analyze', default=None)),
))
    )
    '''Arguments:

    * `sku` (`String`)
    * `po_id` (`String`)
    * `analyze` (`Boolean`)
    '''

    order = sgqlc.types.Field(OrderQueryResult, graphql_name='order', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(String), graphql_name='id', default=None)),
        ('analyze', sgqlc.types.Arg(Boolean, graphql_name='analyze', default=None)),
))
    )
    '''Arguments:

    * `id` (`String!`)
    * `analyze` (`Boolean`)
    '''

    orders = sgqlc.types.Field(OrdersQueryResult, graphql_name='orders', args=sgqlc.types.ArgDict((
        ('shop_name', sgqlc.types.Arg(String, graphql_name='shop_name', default=None)),
        ('partner_order_id', sgqlc.types.Arg(String, graphql_name='partner_order_id', default=None)),
        ('order_number', sgqlc.types.Arg(String, graphql_name='order_number', default=None)),
        ('warehouse_id', sgqlc.types.Arg(String, graphql_name='warehouse_id', default=None)),
        ('allocated_warehouse_id', sgqlc.types.Arg(String, graphql_name='allocated_warehouse_id', default=None)),
        ('fulfillment_status', sgqlc.types.Arg(String, graphql_name='fulfillment_status', default=None)),
        ('sku', sgqlc.types.Arg(String, graphql_name='sku', default=None)),
        ('email', sgqlc.types.Arg(String, graphql_name='email', default=None)),
        ('updated_from', sgqlc.types.Arg(ISODateTime, graphql_name='updated_from', default=None)),
        ('updated_to', sgqlc.types.Arg(ISODateTime, graphql_name='updated_to', default=None)),
        ('order_date_from', sgqlc.types.Arg(ISODateTime, graphql_name='order_date_from', default=None)),
        ('order_date_to', sgqlc.types.Arg(ISODateTime, graphql_name='order_date_to', default=None)),
        ('customer_account_id', sgqlc.types.Arg(String, graphql_name='customer_account_id', default=None)),
        ('analyze', sgqlc.types.Arg(Boolean, graphql_name='analyze', default=None)),
))
    )
    '''Arguments:

    * `shop_name` (`String`)
    * `partner_order_id` (`String`)
    * `order_number` (`String`)
    * `warehouse_id` (`String`)
    * `allocated_warehouse_id` (`String`)
    * `fulfillment_status` (`String`)
    * `sku` (`String`)
    * `email` (`String`)
    * `updated_from` (`ISODateTime`)
    * `updated_to` (`ISODateTime`)
    * `order_date_from` (`ISODateTime`)
    * `order_date_to` (`ISODateTime`)
    * `customer_account_id` (`String`)
    * `analyze` (`Boolean`)
    '''

    order_history = sgqlc.types.Field(OrderHistoryQueryResult, graphql_name='order_history', args=sgqlc.types.ArgDict((
        ('order_id', sgqlc.types.Arg(String, graphql_name='order_id', default=None)),
        ('user_id', sgqlc.types.Arg(String, graphql_name='user_id', default=None)),
        ('order_number', sgqlc.types.Arg(String, graphql_name='order_number', default=None)),
        ('username', sgqlc.types.Arg(String, graphql_name='username', default=None)),
        ('date_from', sgqlc.types.Arg(Date, graphql_name='date_from', default=None)),
        ('date_to', sgqlc.types.Arg(Date, graphql_name='date_to', default=None)),
        ('analyze', sgqlc.types.Arg(Boolean, graphql_name='analyze', default=None)),
))
    )
    '''Arguments:

    * `order_id` (`String`)
    * `user_id` (`String`)
    * `order_number` (`String`)
    * `username` (`String`)
    * `date_from` (`Date`)
    * `date_to` (`Date`)
    * `analyze` (`Boolean`)
    '''

    packs_per_day = sgqlc.types.Field(PacksPerDayQueryResult, graphql_name='packs_per_day', args=sgqlc.types.ArgDict((
        ('warehouse_id', sgqlc.types.Arg(String, graphql_name='warehouse_id', default=None)),
        ('user_id', sgqlc.types.Arg(String, graphql_name='user_id', default=None)),
        ('order_id', sgqlc.types.Arg(String, graphql_name='order_id', default=None)),
        ('order_number', sgqlc.types.Arg(String, graphql_name='order_number', default=None)),
        ('date_from', sgqlc.types.Arg(ISODateTime, graphql_name='date_from', default=None)),
        ('date_to', sgqlc.types.Arg(ISODateTime, graphql_name='date_to', default=None)),
        ('analyze', sgqlc.types.Arg(Boolean, graphql_name='analyze', default=None)),
))
    )
    '''Arguments:

    * `warehouse_id` (`String`)
    * `user_id` (`String`)
    * `order_id` (`String`)
    * `order_number` (`String`)
    * `date_from` (`ISODateTime`)
    * `date_to` (`ISODateTime`)
    * `analyze` (`Boolean`)
    '''

    picks_per_day = sgqlc.types.Field(PicksPerDayQueryResult, graphql_name='picks_per_day', args=sgqlc.types.ArgDict((
        ('warehouse_id', sgqlc.types.Arg(String, graphql_name='warehouse_id', default=None)),
        ('date_from', sgqlc.types.Arg(ISODateTime, graphql_name='date_from', default=None)),
        ('date_to', sgqlc.types.Arg(ISODateTime, graphql_name='date_to', default=None)),
        ('analyze', sgqlc.types.Arg(Boolean, graphql_name='analyze', default=None)),
))
    )
    '''Arguments:

    * `warehouse_id` (`String`)
    * `date_from` (`ISODateTime`)
    * `date_to` (`ISODateTime`)
    * `analyze` (`Boolean`)
    '''

    product = sgqlc.types.Field(ProductQueryResult, graphql_name='product', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(String, graphql_name='id', default=None)),
        ('sku', sgqlc.types.Arg(String, graphql_name='sku', default=None)),
        ('analyze', sgqlc.types.Arg(Boolean, graphql_name='analyze', default=None)),
))
    )
    '''Arguments:

    * `id` (`String`)
    * `sku` (`String`)
    * `analyze` (`Boolean`)
    '''

    products = sgqlc.types.Field(ProductsQueryResult, graphql_name='products', args=sgqlc.types.ArgDict((
        ('sku', sgqlc.types.Arg(String, graphql_name='sku', default=None)),
        ('created_from', sgqlc.types.Arg(ISODateTime, graphql_name='created_from', default=None)),
        ('created_to', sgqlc.types.Arg(ISODateTime, graphql_name='created_to', default=None)),
        ('updated_from', sgqlc.types.Arg(ISODateTime, graphql_name='updated_from', default=None)),
        ('updated_to', sgqlc.types.Arg(ISODateTime, graphql_name='updated_to', default=None)),
        ('customer_account_id', sgqlc.types.Arg(String, graphql_name='customer_account_id', default=None)),
        ('analyze', sgqlc.types.Arg(Boolean, graphql_name='analyze', default=None)),
))
    )
    '''Arguments:

    * `sku` (`String`)
    * `created_from` (`ISODateTime`)
    * `created_to` (`ISODateTime`)
    * `updated_from` (`ISODateTime`)
    * `updated_to` (`ISODateTime`)
    * `customer_account_id` (`String`)
    * `analyze` (`Boolean`)
    '''

    warehouse_products = sgqlc.types.Field('WarehouseProductsQueryResult', graphql_name='warehouse_products', args=sgqlc.types.ArgDict((
        ('warehouse_id', sgqlc.types.Arg(String, graphql_name='warehouse_id', default=None)),
        ('active', sgqlc.types.Arg(Boolean, graphql_name='active', default=None)),
        ('sku', sgqlc.types.Arg(String, graphql_name='sku', default=None)),
        ('customer_account_id', sgqlc.types.Arg(String, graphql_name='customer_account_id', default=None)),
        ('created_from', sgqlc.types.Arg(ISODateTime, graphql_name='created_from', default=None)),
        ('created_to', sgqlc.types.Arg(ISODateTime, graphql_name='created_to', default=None)),
        ('updated_from', sgqlc.types.Arg(ISODateTime, graphql_name='updated_from', default=None)),
        ('updated_to', sgqlc.types.Arg(ISODateTime, graphql_name='updated_to', default=None)),
        ('analyze', sgqlc.types.Arg(Boolean, graphql_name='analyze', default=None)),
))
    )
    '''Arguments:

    * `warehouse_id` (`String`)
    * `active` (`Boolean`)
    * `sku` (`String`)
    * `customer_account_id` (`String`)
    * `created_from` (`ISODateTime`)
    * `created_to` (`ISODateTime`)
    * `updated_from` (`ISODateTime`)
    * `updated_to` (`ISODateTime`)
    * `analyze` (`Boolean`)
    '''

    purchase_order = sgqlc.types.Field(PurchaseOrderQueryResult, graphql_name='purchase_order', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(String, graphql_name='id', default=None)),
        ('po_number', sgqlc.types.Arg(String, graphql_name='po_number', default=None)),
        ('analyze', sgqlc.types.Arg(Boolean, graphql_name='analyze', default=None)),
))
    )
    '''Arguments:

    * `id` (`String`)
    * `po_number` (`String`)
    * `analyze` (`Boolean`)
    '''

    purchase_orders = sgqlc.types.Field(PurchaseOrdersQueryResult, graphql_name='purchase_orders', args=sgqlc.types.ArgDict((
        ('sku', sgqlc.types.Arg(String, graphql_name='sku', default=None)),
        ('warehouse_id', sgqlc.types.Arg(String, graphql_name='warehouse_id', default=None)),
        ('created_from', sgqlc.types.Arg(ISODateTime, graphql_name='created_from', default=None)),
        ('created_to', sgqlc.types.Arg(ISODateTime, graphql_name='created_to', default=None)),
        ('po_date_from', sgqlc.types.Arg(ISODateTime, graphql_name='po_date_from', default=None)),
        ('po_date_to', sgqlc.types.Arg(ISODateTime, graphql_name='po_date_to', default=None)),
        ('customer_account_id', sgqlc.types.Arg(String, graphql_name='customer_account_id', default=None)),
        ('analyze', sgqlc.types.Arg(Boolean, graphql_name='analyze', default=None)),
))
    )
    '''Arguments:

    * `sku` (`String`)
    * `warehouse_id` (`String`)
    * `created_from` (`ISODateTime`)
    * `created_to` (`ISODateTime`)
    * `po_date_from` (`ISODateTime`)
    * `po_date_to` (`ISODateTime`)
    * `customer_account_id` (`String`)
    * `analyze` (`Boolean`)
    '''

    return_ = sgqlc.types.Field('ReturnQueryResult', graphql_name='return', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(String), graphql_name='id', default=None)),
        ('analyze', sgqlc.types.Arg(Boolean, graphql_name='analyze', default=None)),
))
    )
    '''Arguments:

    * `id` (`String!`)
    * `analyze` (`Boolean`)
    '''

    returns = sgqlc.types.Field('ReturnsQueryResult', graphql_name='returns', args=sgqlc.types.ArgDict((
        ('order_id', sgqlc.types.Arg(String, graphql_name='order_id', default=None)),
        ('warehouse_id', sgqlc.types.Arg(String, graphql_name='warehouse_id', default=None)),
        ('date_from', sgqlc.types.Arg(ISODateTime, graphql_name='date_from', default=None)),
        ('date_to', sgqlc.types.Arg(ISODateTime, graphql_name='date_to', default=None)),
        ('customer_account_id', sgqlc.types.Arg(String, graphql_name='customer_account_id', default=None)),
        ('analyze', sgqlc.types.Arg(Boolean, graphql_name='analyze', default=None)),
))
    )
    '''Arguments:

    * `order_id` (`String`)
    * `warehouse_id` (`String`)
    * `date_from` (`ISODateTime`)
    * `date_to` (`ISODateTime`)
    * `customer_account_id` (`String`)
    * `analyze` (`Boolean`)
    '''

    return_exchange = sgqlc.types.Field('ReturnExchangeQueryResult', graphql_name='return_exchange', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(String), graphql_name='id', default=None)),
        ('analyze', sgqlc.types.Arg(Boolean, graphql_name='analyze', default=None)),
))
    )
    '''Arguments:

    * `id` (`String!`)
    * `analyze` (`Boolean`)
    '''

    shipment = sgqlc.types.Field('ShipmentQueryResult', graphql_name='shipment', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(String, graphql_name='id', default=None)),
        ('analyze', sgqlc.types.Arg(Boolean, graphql_name='analyze', default=None)),
))
    )
    '''Arguments:

    * `id` (`String`)
    * `analyze` (`Boolean`)
    '''

    shipments = sgqlc.types.Field('ShipmentsQueryResult', graphql_name='shipments', args=sgqlc.types.ArgDict((
        ('order_id', sgqlc.types.Arg(String, graphql_name='order_id', default=None)),
        ('date_from', sgqlc.types.Arg(ISODateTime, graphql_name='date_from', default=None)),
        ('date_to', sgqlc.types.Arg(ISODateTime, graphql_name='date_to', default=None)),
        ('order_date_from', sgqlc.types.Arg(ISODateTime, graphql_name='order_date_from', default=None)),
        ('order_date_to', sgqlc.types.Arg(ISODateTime, graphql_name='order_date_to', default=None)),
        ('analyze', sgqlc.types.Arg(Boolean, graphql_name='analyze', default=None)),
))
    )
    '''Arguments:

    * `order_id` (`String`)
    * `date_from` (`ISODateTime`)
    * `date_to` (`ISODateTime`)
    * `order_date_from` (`ISODateTime`)
    * `order_date_to` (`ISODateTime`)
    * `analyze` (`Boolean`)
    '''

    shipping_plan = sgqlc.types.Field('ShippingPlanQueryResult', graphql_name='shipping_plan', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(String, graphql_name='id', default=None)),
        ('analyze', sgqlc.types.Arg(Boolean, graphql_name='analyze', default=None)),
))
    )
    '''Arguments:

    * `id` (`String`)
    * `analyze` (`Boolean`)
    '''

    tote_history = sgqlc.types.Field('ToteHistoryQueryResult', graphql_name='tote_history', args=sgqlc.types.ArgDict((
        ('tote_name', sgqlc.types.Arg(String, graphql_name='tote_name', default=None)),
        ('tote_id', sgqlc.types.Arg(String, graphql_name='tote_id', default=None)),
        ('date_from', sgqlc.types.Arg(ISODateTime, graphql_name='date_from', default=None)),
        ('date_to', sgqlc.types.Arg(ISODateTime, graphql_name='date_to', default=None)),
        ('analyze', sgqlc.types.Arg(Boolean, graphql_name='analyze', default=None)),
))
    )
    '''Arguments:

    * `tote_name` (`String`)
    * `tote_id` (`String`)
    * `date_from` (`ISODateTime`)
    * `date_to` (`ISODateTime`)
    * `analyze` (`Boolean`)
    '''

    user_quota = sgqlc.types.Field('UserQuota', graphql_name='user_quota')

    vendors = sgqlc.types.Field('VendorsQueryResult', graphql_name='vendors', args=sgqlc.types.ArgDict((
        ('analyze', sgqlc.types.Arg(Boolean, graphql_name='analyze', default=None)),
))
    )
    '''Arguments:

    * `analyze` (`Boolean`)
    '''

    webhooks = sgqlc.types.Field('WebhooksQueryResult', graphql_name='webhooks', args=sgqlc.types.ArgDict((
        ('customer_account_id', sgqlc.types.Arg(String, graphql_name='customer_account_id', default=None)),
        ('analyze', sgqlc.types.Arg(Boolean, graphql_name='analyze', default=None)),
))
    )
    '''Arguments:

    * `customer_account_id` (`String`)
    * `analyze` (`Boolean`)
    '''



class RMALabel(sgqlc.types.Type):
    __schema__ = shiphero_schema
    __field_names__ = ('id', 'legacy_id', 'account_id', 'order_id', 'rma_id', 'shipment_id', 'shipping_name', 'tracking_number', 'status', 'carrier', 'shipping_method', 'cost', 'box_code', 'dimensions', 'address', 'paper_pdf_location', 'thermal_pdf_location', 'pdf_location', 'image_location', 'delivered', 'picked_up', 'refunded', 'needs_refund', 'profile', 'full_size_to_print', 'partner_fulfillment_id', 'created_at', 'updated_at')
    id = sgqlc.types.Field(String, graphql_name='id')

    legacy_id = sgqlc.types.Field(Int, graphql_name='legacy_id')

    account_id = sgqlc.types.Field(String, graphql_name='account_id')

    order_id = sgqlc.types.Field(String, graphql_name='order_id')

    rma_id = sgqlc.types.Field(String, graphql_name='rma_id')

    shipment_id = sgqlc.types.Field(String, graphql_name='shipment_id')

    shipping_name = sgqlc.types.Field(String, graphql_name='shipping_name')

    tracking_number = sgqlc.types.Field(String, graphql_name='tracking_number')

    status = sgqlc.types.Field(String, graphql_name='status')

    carrier = sgqlc.types.Field(String, graphql_name='carrier')

    shipping_method = sgqlc.types.Field(String, graphql_name='shipping_method')

    cost = sgqlc.types.Field(String, graphql_name='cost')

    box_code = sgqlc.types.Field(String, graphql_name='box_code')

    dimensions = sgqlc.types.Field(Dimensions, graphql_name='dimensions')

    address = sgqlc.types.Field(Address, graphql_name='address')

    paper_pdf_location = sgqlc.types.Field(String, graphql_name='paper_pdf_location')

    thermal_pdf_location = sgqlc.types.Field(String, graphql_name='thermal_pdf_location')

    pdf_location = sgqlc.types.Field(String, graphql_name='pdf_location')

    image_location = sgqlc.types.Field(String, graphql_name='image_location')

    delivered = sgqlc.types.Field(Boolean, graphql_name='delivered')

    picked_up = sgqlc.types.Field(Boolean, graphql_name='picked_up')

    refunded = sgqlc.types.Field(Boolean, graphql_name='refunded')

    needs_refund = sgqlc.types.Field(Boolean, graphql_name='needs_refund')

    profile = sgqlc.types.Field(String, graphql_name='profile')

    full_size_to_print = sgqlc.types.Field(String, graphql_name='full_size_to_print')

    partner_fulfillment_id = sgqlc.types.Field(String, graphql_name='partner_fulfillment_id')

    created_at = sgqlc.types.Field(ISODateTime, graphql_name='created_at')

    updated_at = sgqlc.types.Field(ISODateTime, graphql_name='updated_at')



class RecalculateBillOutput(sgqlc.types.Type):
    __schema__ = shiphero_schema
    __field_names__ = ('request_id', 'complexity', 'bill')
    request_id = sgqlc.types.Field(String, graphql_name='request_id')

    complexity = sgqlc.types.Field(Int, graphql_name='complexity')

    bill = sgqlc.types.Field(Bill, graphql_name='bill')



class Return(sgqlc.types.Type):
    __schema__ = shiphero_schema
    __field_names__ = ('id', 'legacy_id', 'account_id', 'order_id', 'partner_id', 'reason', 'status', 'label_type', 'label_cost', 'cost_to_customer', 'shipping_carrier', 'shipping_method', 'dimensions', 'address', 'line_items', 'total_items_expected', 'total_items_received', 'total_items_restocked', 'created_at', 'display_issue_refund', 'order', 'exchanges')
    id = sgqlc.types.Field(String, graphql_name='id')

    legacy_id = sgqlc.types.Field(Int, graphql_name='legacy_id')

    account_id = sgqlc.types.Field(String, graphql_name='account_id')

    order_id = sgqlc.types.Field(String, graphql_name='order_id')

    partner_id = sgqlc.types.Field(String, graphql_name='partner_id')

    reason = sgqlc.types.Field(String, graphql_name='reason')

    status = sgqlc.types.Field(String, graphql_name='status')

    label_type = sgqlc.types.Field(ReturnLabelType, graphql_name='label_type')

    label_cost = sgqlc.types.Field(String, graphql_name='label_cost')

    cost_to_customer = sgqlc.types.Field(String, graphql_name='cost_to_customer')

    shipping_carrier = sgqlc.types.Field(String, graphql_name='shipping_carrier')

    shipping_method = sgqlc.types.Field(String, graphql_name='shipping_method')

    dimensions = sgqlc.types.Field(Dimensions, graphql_name='dimensions')

    address = sgqlc.types.Field(Address, graphql_name='address')

    line_items = sgqlc.types.Field(sgqlc.types.list_of('ReturnLineItem'), graphql_name='line_items')

    total_items_expected = sgqlc.types.Field(Int, graphql_name='total_items_expected')

    total_items_received = sgqlc.types.Field(Int, graphql_name='total_items_received')

    total_items_restocked = sgqlc.types.Field(Int, graphql_name='total_items_restocked')

    created_at = sgqlc.types.Field(ISODateTime, graphql_name='created_at')

    display_issue_refund = sgqlc.types.Field(Boolean, graphql_name='display_issue_refund')

    order = sgqlc.types.Field(Order, graphql_name='order')

    exchanges = sgqlc.types.Field(sgqlc.types.list_of('ReturnExchange'), graphql_name='exchanges')



class ReturnConnection(sgqlc.types.relay.Connection):
    __schema__ = shiphero_schema
    __field_names__ = ('page_info', 'edges')
    page_info = sgqlc.types.Field(sgqlc.types.non_null(PageInfo), graphql_name='pageInfo')

    edges = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of('ReturnEdge')), graphql_name='edges')



class ReturnEdge(sgqlc.types.Type):
    __schema__ = shiphero_schema
    __field_names__ = ('node', 'cursor')
    node = sgqlc.types.Field(Return, graphql_name='node')

    cursor = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='cursor')



class ReturnExchange(sgqlc.types.Type):
    __schema__ = shiphero_schema
    __field_names__ = ('id', 'legacy_id', 'exchange_order_id', 'return_id', 'account_id', 'exchange_order', 'exchange_items', 'original_return')
    id = sgqlc.types.Field(String, graphql_name='id')

    legacy_id = sgqlc.types.Field(Int, graphql_name='legacy_id')

    exchange_order_id = sgqlc.types.Field(String, graphql_name='exchange_order_id')

    return_id = sgqlc.types.Field(String, graphql_name='return_id')

    account_id = sgqlc.types.Field(String, graphql_name='account_id')

    exchange_order = sgqlc.types.Field(Order, graphql_name='exchange_order')

    exchange_items = sgqlc.types.Field(sgqlc.types.list_of('ReturnExchangeItem'), graphql_name='exchange_items')

    original_return = sgqlc.types.Field(Return, graphql_name='original_return')



class ReturnExchangeItem(sgqlc.types.Type):
    __schema__ = shiphero_schema
    __field_names__ = ('id', 'legacy_id', 'return_item_id', 'sku', 'quantity')
    id = sgqlc.types.Field(String, graphql_name='id')

    legacy_id = sgqlc.types.Field(Int, graphql_name='legacy_id')

    return_item_id = sgqlc.types.Field(String, graphql_name='return_item_id')

    sku = sgqlc.types.Field(String, graphql_name='sku')

    quantity = sgqlc.types.Field(Int, graphql_name='quantity')



class ReturnExchangeQueryResult(sgqlc.types.Type):
    __schema__ = shiphero_schema
    __field_names__ = ('request_id', 'complexity', 'data')
    request_id = sgqlc.types.Field(String, graphql_name='request_id')

    complexity = sgqlc.types.Field(Int, graphql_name='complexity')

    data = sgqlc.types.Field(ReturnExchange, graphql_name='data')



class ReturnLineItem(sgqlc.types.Type):
    __schema__ = shiphero_schema
    __field_names__ = ('id', 'legacy_id', 'account_id', 'line_item_id', 'warehouse_id', 'product_id', 'return_id', 'quantity', 'quantity_received', 'restock', 'condition', 'is_component', 'type', 'reason', 'created_at', 'updated_at', 'line_item', 'warehouse')
    id = sgqlc.types.Field(String, graphql_name='id')

    legacy_id = sgqlc.types.Field(Int, graphql_name='legacy_id')

    account_id = sgqlc.types.Field(String, graphql_name='account_id')

    line_item_id = sgqlc.types.Field(String, graphql_name='line_item_id')

    warehouse_id = sgqlc.types.Field(String, graphql_name='warehouse_id')

    product_id = sgqlc.types.Field(String, graphql_name='product_id')

    return_id = sgqlc.types.Field(String, graphql_name='return_id')

    quantity = sgqlc.types.Field(Int, graphql_name='quantity')

    quantity_received = sgqlc.types.Field(Int, graphql_name='quantity_received')

    restock = sgqlc.types.Field(Int, graphql_name='restock')

    condition = sgqlc.types.Field(String, graphql_name='condition')

    is_component = sgqlc.types.Field(Boolean, graphql_name='is_component')

    type = sgqlc.types.Field(String, graphql_name='type')

    reason = sgqlc.types.Field(String, graphql_name='reason')

    created_at = sgqlc.types.Field(ISODateTime, graphql_name='created_at')

    updated_at = sgqlc.types.Field(ISODateTime, graphql_name='updated_at')

    line_item = sgqlc.types.Field(LineItem, graphql_name='line_item')

    warehouse = sgqlc.types.Field('Warehouse', graphql_name='warehouse')



class ReturnQueryResult(sgqlc.types.Type):
    __schema__ = shiphero_schema
    __field_names__ = ('request_id', 'complexity', 'data')
    request_id = sgqlc.types.Field(String, graphql_name='request_id')

    complexity = sgqlc.types.Field(Int, graphql_name='complexity')

    data = sgqlc.types.Field(Return, graphql_name='data')



class ReturnsQueryResult(sgqlc.types.Type):
    __schema__ = shiphero_schema
    __field_names__ = ('request_id', 'complexity', 'data')
    request_id = sgqlc.types.Field(String, graphql_name='request_id')

    complexity = sgqlc.types.Field(Int, graphql_name='complexity')

    data = sgqlc.types.Field(ReturnConnection, graphql_name='data', args=sgqlc.types.ArgDict((
        ('sort', sgqlc.types.Arg(String, graphql_name='sort', default=None)),
        ('before', sgqlc.types.Arg(String, graphql_name='before', default=None)),
        ('after', sgqlc.types.Arg(String, graphql_name='after', default=None)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
))
    )
    '''Arguments:

    * `sort` (`String`)
    * `before` (`String`)
    * `after` (`String`)
    * `first` (`Int`)
    * `last` (`Int`)
    '''



class SetPurchaseOrderFulfillmentStatusOutput(sgqlc.types.Type):
    __schema__ = shiphero_schema
    __field_names__ = ('request_id', 'complexity', 'purchase_order')
    request_id = sgqlc.types.Field(String, graphql_name='request_id')

    complexity = sgqlc.types.Field(Int, graphql_name='complexity')

    purchase_order = sgqlc.types.Field(PurchaseOrder, graphql_name='purchase_order')



class Shipment(sgqlc.types.Type):
    __schema__ = shiphero_schema
    __field_names__ = ('id', 'legacy_id', 'order_id', 'user_id', 'warehouse_id', 'pending_shipment_id', 'address', 'profile', 'picked_up', 'needs_refund', 'refunded', 'delivered', 'dropshipment', 'shipped_off_shiphero', 'completed', 'created_date', 'line_items', 'shipping_labels', 'warehouse', 'order')
    id = sgqlc.types.Field(String, graphql_name='id')

    legacy_id = sgqlc.types.Field(Int, graphql_name='legacy_id')

    order_id = sgqlc.types.Field(String, graphql_name='order_id')

    user_id = sgqlc.types.Field(String, graphql_name='user_id')

    warehouse_id = sgqlc.types.Field(String, graphql_name='warehouse_id')

    pending_shipment_id = sgqlc.types.Field(String, graphql_name='pending_shipment_id')

    address = sgqlc.types.Field(Address, graphql_name='address')

    profile = sgqlc.types.Field(String, graphql_name='profile')

    picked_up = sgqlc.types.Field(Boolean, graphql_name='picked_up')

    needs_refund = sgqlc.types.Field(Boolean, graphql_name='needs_refund')

    refunded = sgqlc.types.Field(Boolean, graphql_name='refunded')

    delivered = sgqlc.types.Field(Boolean, graphql_name='delivered')

    dropshipment = sgqlc.types.Field(Boolean, graphql_name='dropshipment')

    shipped_off_shiphero = sgqlc.types.Field(Boolean, graphql_name='shipped_off_shiphero')

    completed = sgqlc.types.Field(Boolean, graphql_name='completed')

    created_date = sgqlc.types.Field(ISODateTime, graphql_name='created_date')

    line_items = sgqlc.types.Field('ShipmentLineItemConnection', graphql_name='line_items', args=sgqlc.types.ArgDict((
        ('sort', sgqlc.types.Arg(String, graphql_name='sort', default=None)),
        ('before', sgqlc.types.Arg(String, graphql_name='before', default=None)),
        ('after', sgqlc.types.Arg(String, graphql_name='after', default=None)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
))
    )
    '''Arguments:

    * `sort` (`String`)
    * `before` (`String`)
    * `after` (`String`)
    * `first` (`Int`)
    * `last` (`Int`)
    '''

    shipping_labels = sgqlc.types.Field(sgqlc.types.list_of('ShippingLabel'), graphql_name='shipping_labels')

    warehouse = sgqlc.types.Field('Warehouse', graphql_name='warehouse')

    order = sgqlc.types.Field(Order, graphql_name='order')



class ShipmentConnection(sgqlc.types.relay.Connection):
    __schema__ = shiphero_schema
    __field_names__ = ('page_info', 'edges')
    page_info = sgqlc.types.Field(sgqlc.types.non_null(PageInfo), graphql_name='pageInfo')

    edges = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of('ShipmentEdge')), graphql_name='edges')



class ShipmentEdge(sgqlc.types.Type):
    __schema__ = shiphero_schema
    __field_names__ = ('node', 'cursor')
    node = sgqlc.types.Field(Shipment, graphql_name='node')

    cursor = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='cursor')



class ShipmentLineItem(sgqlc.types.Type):
    __schema__ = shiphero_schema
    __field_names__ = ('id', 'legacy_id', 'line_item_id', 'shipment_id', 'shipping_label_id', 'quantity', 'line_item')
    id = sgqlc.types.Field(String, graphql_name='id')

    legacy_id = sgqlc.types.Field(Int, graphql_name='legacy_id')

    line_item_id = sgqlc.types.Field(String, graphql_name='line_item_id')

    shipment_id = sgqlc.types.Field(String, graphql_name='shipment_id')

    shipping_label_id = sgqlc.types.Field(String, graphql_name='shipping_label_id')

    quantity = sgqlc.types.Field(Int, graphql_name='quantity')

    line_item = sgqlc.types.Field(LineItem, graphql_name='line_item')



class ShipmentLineItemConnection(sgqlc.types.relay.Connection):
    __schema__ = shiphero_schema
    __field_names__ = ('page_info', 'edges')
    page_info = sgqlc.types.Field(sgqlc.types.non_null(PageInfo), graphql_name='pageInfo')

    edges = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of('ShipmentLineItemEdge')), graphql_name='edges')



class ShipmentLineItemEdge(sgqlc.types.Type):
    __schema__ = shiphero_schema
    __field_names__ = ('node', 'cursor')
    node = sgqlc.types.Field(ShipmentLineItem, graphql_name='node')

    cursor = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='cursor')



class ShipmentQueryResult(sgqlc.types.Type):
    __schema__ = shiphero_schema
    __field_names__ = ('request_id', 'complexity', 'data')
    request_id = sgqlc.types.Field(String, graphql_name='request_id')

    complexity = sgqlc.types.Field(Int, graphql_name='complexity')

    data = sgqlc.types.Field(Shipment, graphql_name='data')



class ShipmentsQueryResult(sgqlc.types.Type):
    __schema__ = shiphero_schema
    __field_names__ = ('request_id', 'complexity', 'data')
    request_id = sgqlc.types.Field(String, graphql_name='request_id')

    complexity = sgqlc.types.Field(Int, graphql_name='complexity')

    data = sgqlc.types.Field(ShipmentConnection, graphql_name='data', args=sgqlc.types.ArgDict((
        ('sort', sgqlc.types.Arg(String, graphql_name='sort', default=None)),
        ('before', sgqlc.types.Arg(String, graphql_name='before', default=None)),
        ('after', sgqlc.types.Arg(String, graphql_name='after', default=None)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
))
    )
    '''Arguments:

    * `sort` (`String`)
    * `before` (`String`)
    * `after` (`String`)
    * `first` (`Int`)
    * `last` (`Int`)
    '''



class ShippedLineItemLot(sgqlc.types.Type):
    __schema__ = shiphero_schema
    __field_names__ = ('id', 'legacy_id', 'line_item_id', 'lot_id', 'lot_name', 'lot_expiration_date')
    id = sgqlc.types.Field(String, graphql_name='id')

    legacy_id = sgqlc.types.Field(Int, graphql_name='legacy_id')

    line_item_id = sgqlc.types.Field(String, graphql_name='line_item_id')

    lot_id = sgqlc.types.Field(String, graphql_name='lot_id')

    lot_name = sgqlc.types.Field(String, graphql_name='lot_name')

    lot_expiration_date = sgqlc.types.Field(ISODateTime, graphql_name='lot_expiration_date')



class ShippingLabel(sgqlc.types.Type):
    __schema__ = shiphero_schema
    __field_names__ = ('id', 'legacy_id', 'account_id', 'shipment_id', 'order_id', 'box_id', 'status', 'tracking_number', 'order_number', 'order_account_id', 'carrier', 'shipping_name', 'shipping_method', 'cost', 'box_code', 'device_id', 'delivered', 'picked_up', 'refunded', 'needs_refund', 'profile', 'partner_fulfillment_id', 'full_size_to_print', 'packing_slip', 'warehouse', 'warehouse_id', 'insurance_amount', 'carrier_account_id', 'source', 'created_date', 'dimensions', 'label', 'address', 'order', 'shipment_line_items')
    id = sgqlc.types.Field(String, graphql_name='id')

    legacy_id = sgqlc.types.Field(Int, graphql_name='legacy_id')

    account_id = sgqlc.types.Field(String, graphql_name='account_id')

    shipment_id = sgqlc.types.Field(String, graphql_name='shipment_id')

    order_id = sgqlc.types.Field(String, graphql_name='order_id')

    box_id = sgqlc.types.Field(String, graphql_name='box_id')

    status = sgqlc.types.Field(String, graphql_name='status')

    tracking_number = sgqlc.types.Field(String, graphql_name='tracking_number')

    order_number = sgqlc.types.Field(String, graphql_name='order_number')

    order_account_id = sgqlc.types.Field(String, graphql_name='order_account_id')

    carrier = sgqlc.types.Field(String, graphql_name='carrier')

    shipping_name = sgqlc.types.Field(String, graphql_name='shipping_name')

    shipping_method = sgqlc.types.Field(String, graphql_name='shipping_method')

    cost = sgqlc.types.Field(String, graphql_name='cost')

    box_code = sgqlc.types.Field(String, graphql_name='box_code')

    device_id = sgqlc.types.Field(String, graphql_name='device_id')

    delivered = sgqlc.types.Field(Boolean, graphql_name='delivered')

    picked_up = sgqlc.types.Field(Boolean, graphql_name='picked_up')

    refunded = sgqlc.types.Field(Boolean, graphql_name='refunded')

    needs_refund = sgqlc.types.Field(Boolean, graphql_name='needs_refund')

    profile = sgqlc.types.Field(String, graphql_name='profile')

    partner_fulfillment_id = sgqlc.types.Field(String, graphql_name='partner_fulfillment_id')

    full_size_to_print = sgqlc.types.Field(String, graphql_name='full_size_to_print')

    packing_slip = sgqlc.types.Field(String, graphql_name='packing_slip')

    warehouse = sgqlc.types.Field(String, graphql_name='warehouse')

    warehouse_id = sgqlc.types.Field(String, graphql_name='warehouse_id')

    insurance_amount = sgqlc.types.Field(String, graphql_name='insurance_amount')

    carrier_account_id = sgqlc.types.Field(String, graphql_name='carrier_account_id')

    source = sgqlc.types.Field(String, graphql_name='source')

    created_date = sgqlc.types.Field(ISODateTime, graphql_name='created_date')

    dimensions = sgqlc.types.Field(Dimensions, graphql_name='dimensions')

    label = sgqlc.types.Field(LabelResource, graphql_name='label')

    address = sgqlc.types.Field(Address, graphql_name='address')

    order = sgqlc.types.Field(Order, graphql_name='order')

    shipment_line_items = sgqlc.types.Field(ShipmentLineItemConnection, graphql_name='shipment_line_items', args=sgqlc.types.ArgDict((
        ('sort', sgqlc.types.Arg(String, graphql_name='sort', default=None)),
        ('before', sgqlc.types.Arg(String, graphql_name='before', default=None)),
        ('after', sgqlc.types.Arg(String, graphql_name='after', default=None)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
))
    )
    '''Arguments:

    * `sort` (`String`)
    * `before` (`String`)
    * `after` (`String`)
    * `first` (`Int`)
    * `last` (`Int`)
    '''



class ShippingLines(sgqlc.types.Type):
    __schema__ = shiphero_schema
    __field_names__ = ('title', 'carrier', 'method', 'price')
    title = sgqlc.types.Field(String, graphql_name='title')

    carrier = sgqlc.types.Field(String, graphql_name='carrier')

    method = sgqlc.types.Field(String, graphql_name='method')

    price = sgqlc.types.Field(String, graphql_name='price')



class ShippingPlan(sgqlc.types.Type):
    __schema__ = shiphero_schema
    __field_names__ = ('id', 'legacy_id', 'account_id', 'warehouse_id', 'created_at', 'fulfillment_status', 'warehouse_note', 'vendor_po_number', 'subtotal', 'shipping_price', 'total_price', 'shipping_method', 'shipping_carrier', 'shipping_name', 'tracking_number', 'warehouse', 'pdf_location', 'line_items', 'packages', 'pallets', 'origin_of_shipment', 'tracking_numbers')
    id = sgqlc.types.Field(String, graphql_name='id')

    legacy_id = sgqlc.types.Field(Int, graphql_name='legacy_id')

    account_id = sgqlc.types.Field(String, graphql_name='account_id')

    warehouse_id = sgqlc.types.Field(String, graphql_name='warehouse_id')

    created_at = sgqlc.types.Field(ISODateTime, graphql_name='created_at')

    fulfillment_status = sgqlc.types.Field(String, graphql_name='fulfillment_status')

    warehouse_note = sgqlc.types.Field(String, graphql_name='warehouse_note')

    vendor_po_number = sgqlc.types.Field(String, graphql_name='vendor_po_number')

    subtotal = sgqlc.types.Field(String, graphql_name='subtotal')

    shipping_price = sgqlc.types.Field(String, graphql_name='shipping_price')

    total_price = sgqlc.types.Field(String, graphql_name='total_price')

    shipping_method = sgqlc.types.Field(String, graphql_name='shipping_method')

    shipping_carrier = sgqlc.types.Field(String, graphql_name='shipping_carrier')

    shipping_name = sgqlc.types.Field(String, graphql_name='shipping_name')

    tracking_number = sgqlc.types.Field(String, graphql_name='tracking_number')

    warehouse = sgqlc.types.Field('Warehouse', graphql_name='warehouse')

    pdf_location = sgqlc.types.Field(String, graphql_name='pdf_location')

    line_items = sgqlc.types.Field('ShippingPlanLineItemConnection', graphql_name='line_items', args=sgqlc.types.ArgDict((
        ('sort', sgqlc.types.Arg(String, graphql_name='sort', default=None)),
        ('before', sgqlc.types.Arg(String, graphql_name='before', default=None)),
        ('after', sgqlc.types.Arg(String, graphql_name='after', default=None)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
))
    )
    '''Arguments:

    * `sort` (`String`)
    * `before` (`String`)
    * `after` (`String`)
    * `first` (`Int`)
    * `last` (`Int`)
    '''

    packages = sgqlc.types.Field('ShippingPlanPackageConnection', graphql_name='packages', args=sgqlc.types.ArgDict((
        ('sort', sgqlc.types.Arg(String, graphql_name='sort', default=None)),
        ('before', sgqlc.types.Arg(String, graphql_name='before', default=None)),
        ('after', sgqlc.types.Arg(String, graphql_name='after', default=None)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
))
    )
    '''Arguments:

    * `sort` (`String`)
    * `before` (`String`)
    * `after` (`String`)
    * `first` (`Int`)
    * `last` (`Int`)
    '''

    pallets = sgqlc.types.Field('ShippingPlanPalletConnection', graphql_name='pallets', args=sgqlc.types.ArgDict((
        ('sort', sgqlc.types.Arg(String, graphql_name='sort', default=None)),
        ('before', sgqlc.types.Arg(String, graphql_name='before', default=None)),
        ('after', sgqlc.types.Arg(String, graphql_name='after', default=None)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
))
    )
    '''Arguments:

    * `sort` (`String`)
    * `before` (`String`)
    * `after` (`String`)
    * `first` (`Int`)
    * `last` (`Int`)
    '''

    origin_of_shipment = sgqlc.types.Field(String, graphql_name='origin_of_shipment')

    tracking_numbers = sgqlc.types.Field('ShippingPlanTrackingNumberConnection', graphql_name='tracking_numbers', args=sgqlc.types.ArgDict((
        ('sort', sgqlc.types.Arg(String, graphql_name='sort', default=None)),
        ('before', sgqlc.types.Arg(String, graphql_name='before', default=None)),
        ('after', sgqlc.types.Arg(String, graphql_name='after', default=None)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
))
    )
    '''Arguments:

    * `sort` (`String`)
    * `before` (`String`)
    * `after` (`String`)
    * `first` (`Int`)
    * `last` (`Int`)
    '''



class ShippingPlanLineItem(sgqlc.types.Type):
    __schema__ = shiphero_schema
    __field_names__ = ('id', 'legacy_id', 'account_id', 'warehouse_id', 'sku', 'vendor_sku', 'product_id', 'variant_id', 'quantity', 'quantity_received', 'quantity_rejected', 'price', 'product_name', 'option_title', 'expected_weight_in_lbs', 'fulfillment_status', 'sell_ahead', 'note', 'partner_line_item_id', 'barcode', 'updated_at', 'created_at', 'product')
    id = sgqlc.types.Field(String, graphql_name='id')

    legacy_id = sgqlc.types.Field(Int, graphql_name='legacy_id')

    account_id = sgqlc.types.Field(String, graphql_name='account_id')

    warehouse_id = sgqlc.types.Field(String, graphql_name='warehouse_id')

    sku = sgqlc.types.Field(String, graphql_name='sku')

    vendor_sku = sgqlc.types.Field(String, graphql_name='vendor_sku')

    product_id = sgqlc.types.Field(String, graphql_name='product_id')

    variant_id = sgqlc.types.Field(Int, graphql_name='variant_id')

    quantity = sgqlc.types.Field(Int, graphql_name='quantity')

    quantity_received = sgqlc.types.Field(Int, graphql_name='quantity_received')

    quantity_rejected = sgqlc.types.Field(Int, graphql_name='quantity_rejected')

    price = sgqlc.types.Field(String, graphql_name='price')

    product_name = sgqlc.types.Field(String, graphql_name='product_name')

    option_title = sgqlc.types.Field(String, graphql_name='option_title')

    expected_weight_in_lbs = sgqlc.types.Field(String, graphql_name='expected_weight_in_lbs')

    fulfillment_status = sgqlc.types.Field(String, graphql_name='fulfillment_status')

    sell_ahead = sgqlc.types.Field(Int, graphql_name='sell_ahead')

    note = sgqlc.types.Field(String, graphql_name='note')

    partner_line_item_id = sgqlc.types.Field(String, graphql_name='partner_line_item_id')

    barcode = sgqlc.types.Field(String, graphql_name='barcode')

    updated_at = sgqlc.types.Field(ISODateTime, graphql_name='updated_at')

    created_at = sgqlc.types.Field(ISODateTime, graphql_name='created_at')

    product = sgqlc.types.Field('WarehouseProduct', graphql_name='product')



class ShippingPlanLineItemConnection(sgqlc.types.relay.Connection):
    __schema__ = shiphero_schema
    __field_names__ = ('page_info', 'edges')
    page_info = sgqlc.types.Field(sgqlc.types.non_null(PageInfo), graphql_name='pageInfo')

    edges = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of('ShippingPlanLineItemEdge')), graphql_name='edges')



class ShippingPlanLineItemEdge(sgqlc.types.Type):
    __schema__ = shiphero_schema
    __field_names__ = ('node', 'cursor')
    node = sgqlc.types.Field(ShippingPlanLineItem, graphql_name='node')

    cursor = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='cursor')



class ShippingPlanPackage(sgqlc.types.Type):
    __schema__ = shiphero_schema
    __field_names__ = ('id', 'legacy_id', 'box_number', 'line_items')
    id = sgqlc.types.Field(String, graphql_name='id')

    legacy_id = sgqlc.types.Field(Int, graphql_name='legacy_id')

    box_number = sgqlc.types.Field(String, graphql_name='box_number')

    line_items = sgqlc.types.Field('ShippingPlanPackageLineItemConnection', graphql_name='line_items', args=sgqlc.types.ArgDict((
        ('sort', sgqlc.types.Arg(String, graphql_name='sort', default=None)),
        ('before', sgqlc.types.Arg(String, graphql_name='before', default=None)),
        ('after', sgqlc.types.Arg(String, graphql_name='after', default=None)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
))
    )
    '''Arguments:

    * `sort` (`String`)
    * `before` (`String`)
    * `after` (`String`)
    * `first` (`Int`)
    * `last` (`Int`)
    '''



class ShippingPlanPackageConnection(sgqlc.types.relay.Connection):
    __schema__ = shiphero_schema
    __field_names__ = ('page_info', 'edges')
    page_info = sgqlc.types.Field(sgqlc.types.non_null(PageInfo), graphql_name='pageInfo')

    edges = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of('ShippingPlanPackageEdge')), graphql_name='edges')



class ShippingPlanPackageEdge(sgqlc.types.Type):
    __schema__ = shiphero_schema
    __field_names__ = ('node', 'cursor')
    node = sgqlc.types.Field(ShippingPlanPackage, graphql_name='node')

    cursor = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='cursor')



class ShippingPlanPackageLineItem(sgqlc.types.Type):
    __schema__ = shiphero_schema
    __field_names__ = ('id', 'legacy_id', 'sku', 'quantity', 'created_at', 'product')
    id = sgqlc.types.Field(String, graphql_name='id')

    legacy_id = sgqlc.types.Field(Int, graphql_name='legacy_id')

    sku = sgqlc.types.Field(String, graphql_name='sku')

    quantity = sgqlc.types.Field(Int, graphql_name='quantity')

    created_at = sgqlc.types.Field(ISODateTime, graphql_name='created_at')

    product = sgqlc.types.Field(Product, graphql_name='product')



class ShippingPlanPackageLineItemConnection(sgqlc.types.relay.Connection):
    __schema__ = shiphero_schema
    __field_names__ = ('page_info', 'edges')
    page_info = sgqlc.types.Field(sgqlc.types.non_null(PageInfo), graphql_name='pageInfo')

    edges = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of('ShippingPlanPackageLineItemEdge')), graphql_name='edges')



class ShippingPlanPackageLineItemEdge(sgqlc.types.Type):
    __schema__ = shiphero_schema
    __field_names__ = ('node', 'cursor')
    node = sgqlc.types.Field(ShippingPlanPackageLineItem, graphql_name='node')

    cursor = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='cursor')



class ShippingPlanPallet(sgqlc.types.Type):
    __schema__ = shiphero_schema
    __field_names__ = ('id', 'legacy_id', 'kind', 'quantity', 'floor_loaded', 'page_size')
    id = sgqlc.types.Field(String, graphql_name='id')

    legacy_id = sgqlc.types.Field(Int, graphql_name='legacy_id')

    kind = sgqlc.types.Field(String, graphql_name='kind')

    quantity = sgqlc.types.Field(Int, graphql_name='quantity')

    floor_loaded = sgqlc.types.Field(Boolean, graphql_name='floor_loaded')

    page_size = sgqlc.types.Field(String, graphql_name='page_size')



class ShippingPlanPalletConnection(sgqlc.types.relay.Connection):
    __schema__ = shiphero_schema
    __field_names__ = ('page_info', 'edges')
    page_info = sgqlc.types.Field(sgqlc.types.non_null(PageInfo), graphql_name='pageInfo')

    edges = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of('ShippingPlanPalletEdge')), graphql_name='edges')



class ShippingPlanPalletEdge(sgqlc.types.Type):
    __schema__ = shiphero_schema
    __field_names__ = ('node', 'cursor')
    node = sgqlc.types.Field(ShippingPlanPallet, graphql_name='node')

    cursor = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='cursor')



class ShippingPlanQueryResult(sgqlc.types.Type):
    __schema__ = shiphero_schema
    __field_names__ = ('request_id', 'complexity', 'data')
    request_id = sgqlc.types.Field(String, graphql_name='request_id')

    complexity = sgqlc.types.Field(Int, graphql_name='complexity')

    data = sgqlc.types.Field(ShippingPlan, graphql_name='data')



class ShippingPlanTrackingNumber(sgqlc.types.Type):
    __schema__ = shiphero_schema
    __field_names__ = ('id', 'legacy_id', 'po_id', 'carrier_id', 'carrier_value', 'tracking_number')
    id = sgqlc.types.Field(String, graphql_name='id')

    legacy_id = sgqlc.types.Field(Int, graphql_name='legacy_id')

    po_id = sgqlc.types.Field(String, graphql_name='po_id')

    carrier_id = sgqlc.types.Field(String, graphql_name='carrier_id')

    carrier_value = sgqlc.types.Field(String, graphql_name='carrier_value')

    tracking_number = sgqlc.types.Field(String, graphql_name='tracking_number')



class ShippingPlanTrackingNumberConnection(sgqlc.types.relay.Connection):
    __schema__ = shiphero_schema
    __field_names__ = ('page_info', 'edges')
    page_info = sgqlc.types.Field(sgqlc.types.non_null(PageInfo), graphql_name='pageInfo')

    edges = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of('ShippingPlanTrackingNumberEdge')), graphql_name='edges')



class ShippingPlanTrackingNumberEdge(sgqlc.types.Type):
    __schema__ = shiphero_schema
    __field_names__ = ('node', 'cursor')
    node = sgqlc.types.Field(ShippingPlanTrackingNumber, graphql_name='node')

    cursor = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='cursor')



class ToteHistory(sgqlc.types.Type):
    __schema__ = shiphero_schema
    __field_names__ = ('tote_name', 'tote_id', 'action', 'created_at')
    tote_name = sgqlc.types.Field(String, graphql_name='tote_name')

    tote_id = sgqlc.types.Field(String, graphql_name='tote_id')

    action = sgqlc.types.Field(String, graphql_name='action')

    created_at = sgqlc.types.Field(ISODateTime, graphql_name='created_at')



class ToteHistoryConnection(sgqlc.types.relay.Connection):
    __schema__ = shiphero_schema
    __field_names__ = ('page_info', 'edges')
    page_info = sgqlc.types.Field(sgqlc.types.non_null(PageInfo), graphql_name='pageInfo')

    edges = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of('ToteHistoryEdge')), graphql_name='edges')



class ToteHistoryEdge(sgqlc.types.Type):
    __schema__ = shiphero_schema
    __field_names__ = ('node', 'cursor')
    node = sgqlc.types.Field(ToteHistory, graphql_name='node')

    cursor = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='cursor')



class ToteHistoryQueryResult(sgqlc.types.Type):
    __schema__ = shiphero_schema
    __field_names__ = ('request_id', 'complexity', 'data')
    request_id = sgqlc.types.Field(String, graphql_name='request_id')

    complexity = sgqlc.types.Field(Int, graphql_name='complexity')

    data = sgqlc.types.Field(ToteHistoryConnection, graphql_name='data', args=sgqlc.types.ArgDict((
        ('sort', sgqlc.types.Arg(String, graphql_name='sort', default=None)),
        ('before', sgqlc.types.Arg(String, graphql_name='before', default=None)),
        ('after', sgqlc.types.Arg(String, graphql_name='after', default=None)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
))
    )
    '''Arguments:

    * `sort` (`String`)
    * `before` (`String`)
    * `after` (`String`)
    * `first` (`Int`)
    * `last` (`Int`)
    '''



class TotePick(sgqlc.types.Type):
    __schema__ = shiphero_schema
    __field_names__ = ('created_at', 'updated_at', 'tote_id', 'current', 'picked_quantity', 'quantity', 'inventory_bin', 'location_id')
    created_at = sgqlc.types.Field(ISODateTime, graphql_name='created_at')

    updated_at = sgqlc.types.Field(ISODateTime, graphql_name='updated_at')

    tote_id = sgqlc.types.Field(String, graphql_name='tote_id')

    current = sgqlc.types.Field(Int, graphql_name='current')

    picked_quantity = sgqlc.types.Field(Int, graphql_name='picked_quantity')

    quantity = sgqlc.types.Field(Int, graphql_name='quantity')

    inventory_bin = sgqlc.types.Field(String, graphql_name='inventory_bin')

    location_id = sgqlc.types.Field(Int, graphql_name='location_id')



class UpdateInventoryOutput(sgqlc.types.Type):
    __schema__ = shiphero_schema
    __field_names__ = ('request_id', 'complexity', 'warehouse_product')
    request_id = sgqlc.types.Field(String, graphql_name='request_id')

    complexity = sgqlc.types.Field(Int, graphql_name='complexity')

    warehouse_product = sgqlc.types.Field('WarehouseProduct', graphql_name='warehouse_product')



class UpdateLotOutput(sgqlc.types.Type):
    __schema__ = shiphero_schema
    __field_names__ = ('request_id', 'complexity', 'lot')
    request_id = sgqlc.types.Field(String, graphql_name='request_id')

    complexity = sgqlc.types.Field(Int, graphql_name='complexity')

    lot = sgqlc.types.Field(Lot, graphql_name='lot')



class UpdateLotsOutput(sgqlc.types.Type):
    __schema__ = shiphero_schema
    __field_names__ = ('request_id', 'complexity', 'ok')
    request_id = sgqlc.types.Field(String, graphql_name='request_id')

    complexity = sgqlc.types.Field(Int, graphql_name='complexity')

    ok = sgqlc.types.Field(Boolean, graphql_name='ok')



class UpdatePurchaseOrderOutput(sgqlc.types.Type):
    __schema__ = shiphero_schema
    __field_names__ = ('request_id', 'complexity', 'purchase_order')
    request_id = sgqlc.types.Field(String, graphql_name='request_id')

    complexity = sgqlc.types.Field(Int, graphql_name='complexity')

    purchase_order = sgqlc.types.Field(PurchaseOrder, graphql_name='purchase_order')



class UpdateReturnStatusOutput(sgqlc.types.Type):
    __schema__ = shiphero_schema
    __field_names__ = ('request_id', 'complexity', 'return_')
    request_id = sgqlc.types.Field(String, graphql_name='request_id')

    complexity = sgqlc.types.Field(Int, graphql_name='complexity')

    return_ = sgqlc.types.Field(Return, graphql_name='return')



class User(sgqlc.types.Type):
    __schema__ = shiphero_schema
    __field_names__ = ('id', 'legacy_id', 'email', 'first_name', 'last_name', 'account')
    id = sgqlc.types.Field(String, graphql_name='id')

    legacy_id = sgqlc.types.Field(Int, graphql_name='legacy_id')

    email = sgqlc.types.Field(String, graphql_name='email')

    first_name = sgqlc.types.Field(String, graphql_name='first_name')

    last_name = sgqlc.types.Field(String, graphql_name='last_name')

    account = sgqlc.types.Field(Account, graphql_name='account')



class UserQuota(sgqlc.types.Type):
    __schema__ = shiphero_schema
    __field_names__ = ('credits_remaining', 'max_available', 'increment_rate')
    credits_remaining = sgqlc.types.Field(Int, graphql_name='credits_remaining')

    max_available = sgqlc.types.Field(Int, graphql_name='max_available')

    increment_rate = sgqlc.types.Field(Int, graphql_name='increment_rate')



class Vendor(sgqlc.types.Type):
    __schema__ = shiphero_schema
    __field_names__ = ('id', 'legacy_id', 'name', 'email', 'account_number', 'account_id', 'address', 'currency', 'internal_note', 'default_po_note', 'logo', 'partner_vendor_id', 'created_at')
    id = sgqlc.types.Field(String, graphql_name='id')

    legacy_id = sgqlc.types.Field(Int, graphql_name='legacy_id')

    name = sgqlc.types.Field(String, graphql_name='name')

    email = sgqlc.types.Field(String, graphql_name='email')

    account_number = sgqlc.types.Field(String, graphql_name='account_number')

    account_id = sgqlc.types.Field(String, graphql_name='account_id')

    address = sgqlc.types.Field(Address, graphql_name='address')

    currency = sgqlc.types.Field(String, graphql_name='currency')

    internal_note = sgqlc.types.Field(String, graphql_name='internal_note')

    default_po_note = sgqlc.types.Field(String, graphql_name='default_po_note')

    logo = sgqlc.types.Field(String, graphql_name='logo')

    partner_vendor_id = sgqlc.types.Field(Int, graphql_name='partner_vendor_id')

    created_at = sgqlc.types.Field(ISODateTime, graphql_name='created_at')



class VendorConnection(sgqlc.types.relay.Connection):
    __schema__ = shiphero_schema
    __field_names__ = ('page_info', 'edges')
    page_info = sgqlc.types.Field(sgqlc.types.non_null(PageInfo), graphql_name='pageInfo')

    edges = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of('VendorEdge')), graphql_name='edges')



class VendorEdge(sgqlc.types.Type):
    __schema__ = shiphero_schema
    __field_names__ = ('node', 'cursor')
    node = sgqlc.types.Field(Vendor, graphql_name='node')

    cursor = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='cursor')



class VendorsQueryResult(sgqlc.types.Type):
    __schema__ = shiphero_schema
    __field_names__ = ('request_id', 'complexity', 'data')
    request_id = sgqlc.types.Field(String, graphql_name='request_id')

    complexity = sgqlc.types.Field(Int, graphql_name='complexity')

    data = sgqlc.types.Field(VendorConnection, graphql_name='data', args=sgqlc.types.ArgDict((
        ('sort', sgqlc.types.Arg(String, graphql_name='sort', default=None)),
        ('before', sgqlc.types.Arg(String, graphql_name='before', default=None)),
        ('after', sgqlc.types.Arg(String, graphql_name='after', default=None)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
))
    )
    '''Arguments:

    * `sort` (`String`)
    * `before` (`String`)
    * `after` (`String`)
    * `first` (`Int`)
    * `last` (`Int`)
    '''



class Warehouse(sgqlc.types.Type):
    __schema__ = shiphero_schema
    __field_names__ = ('id', 'legacy_id', 'account_id', 'identifier', 'dynamic_slotting', 'invoice_email', 'phone_number', 'profile', 'address', 'return_address', 'company_name', 'company_alias', 'products')
    id = sgqlc.types.Field(String, graphql_name='id')

    legacy_id = sgqlc.types.Field(Int, graphql_name='legacy_id')

    account_id = sgqlc.types.Field(String, graphql_name='account_id')

    identifier = sgqlc.types.Field(String, graphql_name='identifier')

    dynamic_slotting = sgqlc.types.Field(Boolean, graphql_name='dynamic_slotting')

    invoice_email = sgqlc.types.Field(String, graphql_name='invoice_email')

    phone_number = sgqlc.types.Field(String, graphql_name='phone_number')

    profile = sgqlc.types.Field(String, graphql_name='profile')

    address = sgqlc.types.Field(Address, graphql_name='address')

    return_address = sgqlc.types.Field(Address, graphql_name='return_address')

    company_name = sgqlc.types.Field(String, graphql_name='company_name')

    company_alias = sgqlc.types.Field(String, graphql_name='company_alias')

    products = sgqlc.types.Field(ProductConnection, graphql_name='products', args=sgqlc.types.ArgDict((
        ('sort', sgqlc.types.Arg(String, graphql_name='sort', default=None)),
        ('before', sgqlc.types.Arg(String, graphql_name='before', default=None)),
        ('after', sgqlc.types.Arg(String, graphql_name='after', default=None)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
))
    )
    '''Arguments:

    * `sort` (`String`)
    * `before` (`String`)
    * `after` (`String`)
    * `first` (`Int`)
    * `last` (`Int`)
    '''



class WarehouseProduct(sgqlc.types.Type):
    __schema__ = shiphero_schema
    __field_names__ = ('id', 'legacy_id', 'account_id', 'sku', 'warehouse_id', 'warehouse_identifier', 'price', 'value', 'value_currency', 'on_hand', 'inventory_bin', 'inventory_overstock_bin', 'reserve_inventory', 'replenishment_level', 'reorder_amount', 'reorder_level', 'backorder', 'allocated', 'available', 'non_sellable_quantity', 'custom', 'customs_value', 'created_at', 'updated_at', 'sell_ahead', 'active', 'warehouse', 'product', 'inbounds', 'locations')
    id = sgqlc.types.Field(String, graphql_name='id')

    legacy_id = sgqlc.types.Field(Int, graphql_name='legacy_id')

    account_id = sgqlc.types.Field(String, graphql_name='account_id')

    sku = sgqlc.types.Field(String, graphql_name='sku')

    warehouse_id = sgqlc.types.Field(String, graphql_name='warehouse_id')

    warehouse_identifier = sgqlc.types.Field(String, graphql_name='warehouse_identifier')

    price = sgqlc.types.Field(String, graphql_name='price')

    value = sgqlc.types.Field(String, graphql_name='value')

    value_currency = sgqlc.types.Field(String, graphql_name='value_currency')

    on_hand = sgqlc.types.Field(Int, graphql_name='on_hand')

    inventory_bin = sgqlc.types.Field(String, graphql_name='inventory_bin')

    inventory_overstock_bin = sgqlc.types.Field(String, graphql_name='inventory_overstock_bin')

    reserve_inventory = sgqlc.types.Field(Int, graphql_name='reserve_inventory')

    replenishment_level = sgqlc.types.Field(Int, graphql_name='replenishment_level')

    reorder_amount = sgqlc.types.Field(Int, graphql_name='reorder_amount')

    reorder_level = sgqlc.types.Field(Int, graphql_name='reorder_level')

    backorder = sgqlc.types.Field(Int, graphql_name='backorder')

    allocated = sgqlc.types.Field(Int, graphql_name='allocated')

    available = sgqlc.types.Field(Int, graphql_name='available')

    non_sellable_quantity = sgqlc.types.Field(Int, graphql_name='non_sellable_quantity')

    custom = sgqlc.types.Field(Boolean, graphql_name='custom')

    customs_value = sgqlc.types.Field(String, graphql_name='customs_value')

    created_at = sgqlc.types.Field(ISODateTime, graphql_name='created_at')

    updated_at = sgqlc.types.Field(ISODateTime, graphql_name='updated_at')

    sell_ahead = sgqlc.types.Field(Int, graphql_name='sell_ahead')

    active = sgqlc.types.Field(Boolean, graphql_name='active')

    warehouse = sgqlc.types.Field(Warehouse, graphql_name='warehouse')

    product = sgqlc.types.Field(Product, graphql_name='product')

    inbounds = sgqlc.types.Field('WarehouseProductInboundConnection', graphql_name='inbounds', args=sgqlc.types.ArgDict((
        ('status', sgqlc.types.Arg(String, graphql_name='status', default=None)),
        ('created_from', sgqlc.types.Arg(ISODateTime, graphql_name='created_from', default=None)),
        ('created_to', sgqlc.types.Arg(ISODateTime, graphql_name='created_to', default=None)),
        ('sort', sgqlc.types.Arg(String, graphql_name='sort', default=None)),
        ('before', sgqlc.types.Arg(String, graphql_name='before', default=None)),
        ('after', sgqlc.types.Arg(String, graphql_name='after', default=None)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
))
    )
    '''Arguments:

    * `status` (`String`)
    * `created_from` (`ISODateTime`)
    * `created_to` (`ISODateTime`)
    * `sort` (`String`)
    * `before` (`String`)
    * `after` (`String`)
    * `first` (`Int`)
    * `last` (`Int`)
    '''

    locations = sgqlc.types.Field(ItemLocationConnection, graphql_name='locations', args=sgqlc.types.ArgDict((
        ('customer_account_id', sgqlc.types.Arg(String, graphql_name='customer_account_id', default=None)),
        ('sort', sgqlc.types.Arg(String, graphql_name='sort', default=None)),
        ('before', sgqlc.types.Arg(String, graphql_name='before', default=None)),
        ('after', sgqlc.types.Arg(String, graphql_name='after', default=None)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
))
    )
    '''Arguments:

    * `customer_account_id` (`String`)
    * `sort` (`String`)
    * `before` (`String`)
    * `after` (`String`)
    * `first` (`Int`)
    * `last` (`Int`)
    '''



class WarehouseProductConnection(sgqlc.types.relay.Connection):
    __schema__ = shiphero_schema
    __field_names__ = ('page_info', 'edges')
    page_info = sgqlc.types.Field(sgqlc.types.non_null(PageInfo), graphql_name='pageInfo')

    edges = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of('WarehouseProductEdge')), graphql_name='edges')



class WarehouseProductEdge(sgqlc.types.Type):
    __schema__ = shiphero_schema
    __field_names__ = ('node', 'cursor')
    node = sgqlc.types.Field(WarehouseProduct, graphql_name='node')

    cursor = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='cursor')



class WarehouseProductInbound(sgqlc.types.Type):
    __schema__ = shiphero_schema
    __field_names__ = ('id', 'legacy_id', 'sku', 'warehouse_id', 'po_id', 'purchase_order_line_item_id', 'po_date', 'quantity', 'quantity_received', 'quantity_rejected', 'sell_ahead', 'status')
    id = sgqlc.types.Field(String, graphql_name='id')

    legacy_id = sgqlc.types.Field(Int, graphql_name='legacy_id')

    sku = sgqlc.types.Field(String, graphql_name='sku')

    warehouse_id = sgqlc.types.Field(String, graphql_name='warehouse_id')

    po_id = sgqlc.types.Field(String, graphql_name='po_id')

    purchase_order_line_item_id = sgqlc.types.Field(String, graphql_name='purchase_order_line_item_id')

    po_date = sgqlc.types.Field(ISODateTime, graphql_name='po_date')

    quantity = sgqlc.types.Field(Int, graphql_name='quantity')

    quantity_received = sgqlc.types.Field(Int, graphql_name='quantity_received')

    quantity_rejected = sgqlc.types.Field(Int, graphql_name='quantity_rejected')

    sell_ahead = sgqlc.types.Field(Int, graphql_name='sell_ahead')

    status = sgqlc.types.Field(String, graphql_name='status')



class WarehouseProductInboundConnection(sgqlc.types.relay.Connection):
    __schema__ = shiphero_schema
    __field_names__ = ('page_info', 'edges')
    page_info = sgqlc.types.Field(sgqlc.types.non_null(PageInfo), graphql_name='pageInfo')

    edges = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of('WarehouseProductInboundEdge')), graphql_name='edges')



class WarehouseProductInboundEdge(sgqlc.types.Type):
    __schema__ = shiphero_schema
    __field_names__ = ('node', 'cursor')
    node = sgqlc.types.Field(WarehouseProductInbound, graphql_name='node')

    cursor = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='cursor')



class WarehouseProductMutationOutput(sgqlc.types.Type):
    __schema__ = shiphero_schema
    __field_names__ = ('request_id', 'complexity', 'warehouse_product')
    request_id = sgqlc.types.Field(String, graphql_name='request_id')

    complexity = sgqlc.types.Field(Int, graphql_name='complexity')

    warehouse_product = sgqlc.types.Field(WarehouseProduct, graphql_name='warehouse_product')



class WarehouseProductsQueryResult(sgqlc.types.Type):
    __schema__ = shiphero_schema
    __field_names__ = ('request_id', 'complexity', 'data')
    request_id = sgqlc.types.Field(String, graphql_name='request_id')

    complexity = sgqlc.types.Field(Int, graphql_name='complexity')

    data = sgqlc.types.Field(WarehouseProductConnection, graphql_name='data', args=sgqlc.types.ArgDict((
        ('sort', sgqlc.types.Arg(String, graphql_name='sort', default=None)),
        ('before', sgqlc.types.Arg(String, graphql_name='before', default=None)),
        ('after', sgqlc.types.Arg(String, graphql_name='after', default=None)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
))
    )
    '''Arguments:

    * `sort` (`String`)
    * `before` (`String`)
    * `after` (`String`)
    * `first` (`Int`)
    * `last` (`Int`)
    '''



class Webhook(sgqlc.types.Type):
    __schema__ = shiphero_schema
    __field_names__ = ('id', 'legacy_id', 'account_id', 'shop_name', 'name', 'url', 'source', 'shared_signature_secret')
    id = sgqlc.types.Field(String, graphql_name='id')

    legacy_id = sgqlc.types.Field(Int, graphql_name='legacy_id')

    account_id = sgqlc.types.Field(String, graphql_name='account_id')

    shop_name = sgqlc.types.Field(String, graphql_name='shop_name')

    name = sgqlc.types.Field(String, graphql_name='name')

    url = sgqlc.types.Field(String, graphql_name='url')

    source = sgqlc.types.Field(String, graphql_name='source')

    shared_signature_secret = sgqlc.types.Field(String, graphql_name='shared_signature_secret')



class WebhookConnection(sgqlc.types.relay.Connection):
    __schema__ = shiphero_schema
    __field_names__ = ('page_info', 'edges')
    page_info = sgqlc.types.Field(sgqlc.types.non_null(PageInfo), graphql_name='pageInfo')

    edges = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of('WebhookEdge')), graphql_name='edges')



class WebhookEdge(sgqlc.types.Type):
    __schema__ = shiphero_schema
    __field_names__ = ('node', 'cursor')
    node = sgqlc.types.Field(Webhook, graphql_name='node')

    cursor = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='cursor')



class WebhooksQueryResult(sgqlc.types.Type):
    __schema__ = shiphero_schema
    __field_names__ = ('request_id', 'complexity', 'data')
    request_id = sgqlc.types.Field(String, graphql_name='request_id')

    complexity = sgqlc.types.Field(Int, graphql_name='complexity')

    data = sgqlc.types.Field(WebhookConnection, graphql_name='data', args=sgqlc.types.ArgDict((
        ('sort', sgqlc.types.Arg(String, graphql_name='sort', default=None)),
        ('before', sgqlc.types.Arg(String, graphql_name='before', default=None)),
        ('after', sgqlc.types.Arg(String, graphql_name='after', default=None)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
))
    )
    '''Arguments:

    * `sort` (`String`)
    * `before` (`String`)
    * `after` (`String`)
    * `first` (`Int`)
    * `last` (`Int`)
    '''




########################################################################
# Unions
########################################################################

########################################################################
# Schema Entry Points
########################################################################
shiphero_schema.query_type = Query
shiphero_schema.mutation_type = Mutation
shiphero_schema.subscription_type = None

