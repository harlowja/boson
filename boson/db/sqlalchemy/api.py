# vim: tabstop=4 shiftwidth=4 softtabstop=4

# Copyright 2012 OpenStack LLC.
# All Rights Reserved.
#
#    Licensed under the Apache License, Version 2.0 (the "License"); you may
#    not use this file except in compliance with the License. You may obtain
#    a copy of the License at
#
#         http://www.apache.org/licenses/LICENSE-2.0
#
#    Unless required by applicable law or agreed to in writing, software
#    distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
#    WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
#    License for the specific language governing permissions and limitations
#    under the License.

from boson.db import api
from boson.db import models
from boson.db.sqlalchemy import models as sa_models


class API(api.API):
    def create_session(self, context):
        """
        Create a new session.  This will be stored on the user
        context, and can be used by the database to manage a single
        database connection.

        :param context: The current context for accessing the
                        database.
        """

        pass

    def begin(self, context):
        """
        Begin a transaction.

        :param context: The current context for accessing the
                        database.
        """

        pass

    def commit(self, context):
        """
        End a transaction, committing the changes to the database.

        :param context: The current context for accessing the
                        database.
        """

        pass

    def rollback(self, context):
        """
        End a transaction, rolling back the changes to the database.

        :param context: The current context for accessing the
                        database.
        """

        pass

    def create_service(self, context, name, auth_fields):
        """
        Create a new service.  Raises a Duplicate exception in the
        event that the new service is a duplicate of an existing
        service.

        :param context: The current context for accessing the
                        database.
        :param name: The canonical name of the service, i.e., 'nova',
                     'glance', etc.
        :param auth_fields: A sequence listing the names of the fields
                            of authentication and authorization data
                            that the service passes to Boson to
                            uniquely identify the user.

        :returns: An instance of ``boson.db.models.Service``.
        """

        pass

    def get_service(self, context, id=None, name=None, hints=None):
        """
        Look up a specific service by name or by ID.

        :param context: The current context for accessing the
                        database.
        :param id: The ID of the service to look up.
        :param name: The name of the service to look up.
        :param hints: An optional list of hints indicating which
                      attributes of the model will be required by the
                      calling code.  Only those attributes which
                      reference other fields need be listed, although
                      it is not an error to list other fields.  It is
                      also permissible to indicate deeper levels of
                      access by separating attributes with periods.
                      (In the case of reference fields which are
                      represented as lists, there is no need to use
                      square brackets.)

        Note: exactly one of ``id`` and ``name`` must be provided; if
        neither or both are provided, a TypeError will be raised.  If
        no matching service can be found, a KeyError will be raised.

        :returns: An instance of ``boson.db.models.Service``.
        """

        pass

    def get_services(self, context, hints=None):
        """
        Retrieve a list of all defined services.

        :param context: The current context for accessing the
                        database.
        :param hints: An optional list of hints indicating which
                      attributes of the model will be required by the
                      calling code.  Only those attributes which
                      reference other fields need be listed, although
                      it is not an error to list other fields.  It is
                      also permissible to indicate deeper levels of
                      access by separating attributes with periods.
                      (In the case of reference fields which are
                      represented as lists, there is no need to use
                      square brackets.)

        :returns: A list of instances of ``boson.db.models.Service``.
        """

        pass

    def create_category(self, context, service, name, usage_fset, quota_fsets):
        """
        Create a new category on a service.  Raises a Duplicate
        exception in the event that the new category is a duplicate of
        an existing category for the service.

        :param context: The current context for accessing the
                        database.
        :param service: The service the category is for.  Can be
                        either a ``Service`` object or a UUID of an
                        existing service.
        :param name: The canonical name of the category.
        :param usage_fset: A sequence listing the names of the fields
                           of authentication and authorization data,
                           passed by the service to Boson, which are
                           to be used when looking up a ``Usage``
                           record.
        :param quota_fsets: A list of sequences of the names of the
                            fields of authentication and authorization
                            data, which are to be used when looking up
                            ``Quota`` records.  The list must be in
                            order from the most specific to the least
                            specific.  For instance, this list could
                            contain a set referencing the
                            ``tenant_id``, followed by a set
                            referencing the ``quota_class``, followed
                            by an empty set; in this example, a quota
                            applicable to the tenant would be used in
                            preference to one applicable to the quota
                            class, which would be used in preference
                            to the default quota.

        :returns: An instance of ``boson.db.models.Category``.
        """

        pass

    def get_category(self, context, id=None, service=None, name=None,
                     hints=None):
        """
        Look up a specific category by id or by service and name.

        :param context: The current context for accessing the
                        database.
        :param id: The ID of the category to look up.
        :param service: The ``Service`` or service ID of the service
                        to look up the category in.
        :param name: The name of the category to look up.
        :param hints: An optional list of hints indicating which
                      attributes of the model will be required by the
                      calling code.  Only those attributes which
                      reference other fields need be listed, although
                      it is not an error to list other fields.  It is
                      also permissible to indicate deeper levels of
                      access by separating attributes with periods.
                      (In the case of reference fields which are
                      represented as lists, there is no need to use
                      square brackets.)

        Note: either provide ``id`` or provide both ``service`` and
        ``name``.  If an invalid combination of arguments is provided,
        a TypeError will be raised.  If no matching category can be
        found, a KeyError will be raised.

        :returns: An instance of ``boson.db.models.Category``.
        """

        pass

    def get_categories(self, context, service, hints=None):
        """
        Retrieve a list of all defined categories for a given service.

        :param context: The current context for accessing the
                        database.
        :param service: The ``Service`` or service ID of the service
                        to retrieve the categories for.
        :param hints: An optional list of hints indicating which
                      attributes of the model will be required by the
                      calling code.  Only those attributes which
                      reference other fields need be listed, although
                      it is not an error to list other fields.  It is
                      also permissible to indicate deeper levels of
                      access by separating attributes with periods.
                      (In the case of reference fields which are
                      represented as lists, there is no need to use
                      square brackets.)

        :returns: A list of instances of ``boson.db.models.Category``.
        """

        pass

    def create_resource(self, context, service, category, name, parameters,
                        absolute=False):
        """
        Create a new resource on a service.  Raises a Duplicate
        exception in the event that the new resource is a duplicate of
        an existing resource for the service.

        :param context: The current context for accessing the
                        database.
        :param service: The service the resource is for.  Can be
                        either a ``Service`` object or a UUID of an
                        existing service.
        :param category: The category the resource is in.  Can be
                         either a ``Category`` object or a UUID of an
                         existing category.
        :param name: The canonical name of the resource.
        :param parameters: A sequence listing the names of the fields
                           of resource parameter data, passed by the
                           service to Boson, which are to be used when
                           looking up a ``Usage`` record.  Parameters
                           allow application of limits to resources
                           contained within other resources; that is,
                           if a resource has a limit of 5, using
                           parameter data would allow that limit to be
                           interpreted as 5 per parent resource.
        :param absolute: A boolean indicating whether the resource is
                         "absolute."  An absolute resource does not
                         maintain any usage records or allocate any
                         reservations.  Quota enforcement consists of
                         a simple numerical comparison of the
                         requested delta against the quota limit.
                         This is designed to accommodate ephemeral
                         resources, such as the number of files to
                         inject into a Nova instance on boot.

        :returns: An instance of ``boson.db.models.Resource``.
        """

        pass

    def get_resource(self, context, id=None, service=None, name=None,
                     hints=None):
        """
        Look up a specific resource by id or by service and name.

        :param context: The current context for accessing the
                        database.
        :param id: The ID of the resource to look up.
        :param service: The ``Service`` or service ID of the service
                        to look up the resource in.
        :param name: The name of the resource to look up.
        :param hints: An optional list of hints indicating which
                      attributes of the model will be required by the
                      calling code.  Only those attributes which
                      reference other fields need be listed, although
                      it is not an error to list other fields.  It is
                      also permissible to indicate deeper levels of
                      access by separating attributes with periods.
                      (In the case of reference fields which are
                      represented as lists, there is no need to use
                      square brackets.)

        Note: either provide ``id`` or provide both ``service`` and
        ``name``.  If an invalid combination of arguments is provided,
        a TypeError will be raised.  If no matching resource can be
        found, a KeyError will be raised.

        :returns: An instance of ``boson.db.models.Resource``.
        """

        pass

    def get_resources(self, context, service, hints=None):
        """
        Retrieve a list of all defined resources for a given service.

        :param context: The current context for accessing the
                        database.
        :param service: The ``Service`` or service ID of the service
                        to retrieve the resources for.
        :param hints: An optional list of hints indicating which
                      attributes of the model will be required by the
                      calling code.  Only those attributes which
                      reference other fields need be listed, although
                      it is not an error to list other fields.  It is
                      also permissible to indicate deeper levels of
                      access by separating attributes with periods.
                      (In the case of reference fields which are
                      represented as lists, there is no need to use
                      square brackets.)

        :returns: A list of instances of ``boson.db.models.Resource``.
        """

        pass

    def create_usage(self, context, resource, param_data, auth_data, used=0,
                     reserved=0, until_refresh=0, refresh_id=None):
        """
        Create a new usage for a given resource and user.  Raises a
        Duplicate exception in the event that the new usage is a
        duplicate of an existing usage.

        :param context: The current context for accessing the
                        database.
        :param resource: The resource the usage is for.  Can be either
                         a ``Resource`` object or a UUID of an
                         existing resource.
        :param param_data: Resource parameter data (a dictionary).
                           This is used to allow for usages of
                           resources which are children of another
                           resource, where the limit should apply only
                           within that parent resource.  This allows,
                           for example, a restriction on the number of
                           IP addresses for a given Nova instance,
                           without limiting the total number of IP
                           addresses that can be allocated.
        :param auth_data: Authentication and authorization data (a
                          dictionary).  This is used to match up a
                          usage with a particular user of the system.
        :param used: The amount of the resource currently in use.
                     Defaults to 0.
        :param reserved: The amount of the resource currently
                         reserved.  Note that negative reservations
                         are not counted here.  Defaults to 0.
        :param until_refresh: A counter which decrements each time the
                              usage record is used in a quota
                              computation.  When it reaches 0, the
                              usage record will be refreshed.
                              Defaults to 0.
        :param refresh_id: A UUID generated when the usage record
                           needs refreshing.  Refreshed usage
                           information will only be accepted if the
                           refresh has the same ID as stored in this
                           field.  Defaults to None.

        :returns: An instance of ``boson.db.models.Usage``.
        """

        pass

    def get_usage(self, context, id=None, resource=None, param_data=None,
                  auth_data=None, hints=None):
        """
        Look up a specific usage by id or by resource, parameter data,
        and authentication and authorization data.

        :param context: The current context for accessing the
                        database.
        :param id: The ID of the usage to look up.
        :param resource: The ``Resource`` or resource ID of the
                         resource to look up the usage for.
        :param param_data: Resource parameter data (a dictionary).
        :param auth_data: Authentication and authorization data (a
                          dictionary).
        :param hints: An optional list of hints indicating which
                      attributes of the model will be required by the
                      calling code.  Only those attributes which
                      reference other fields need be listed, although
                      it is not an error to list other fields.  It is
                      also permissible to indicate deeper levels of
                      access by separating attributes with periods.
                      (In the case of reference fields which are
                      represented as lists, there is no need to use
                      square brackets.)

        Note: either provide ``id`` or provide all three of
        ``resource``, ``param_data``, and ``auth_data``.  If an
        invalid combination of arguments is provided, a TypeError will
        be raised.  If no matching resource can be found, a KeyError
        will be raised.

        :returns: An instance of ``boson.db.models.Usage``.
        """

        pass

    def get_usages(self, context, resource=None, param_data=None,
                   auth_data=None, hints=None):
        """
        Retrieve a list of all defined usages.

        :param context: The current context for accessing the
                        database.
        :param resource: A ``Service`` or service ID to filter the
                         list of returned usages.
        :param param_data: Resource parameter data (a dictionary) to
                           filter the list of returned usages.  Should
                           be used in conjunction with the
                           ``resource`` filter.
        :param auth_data: Authentication and authorization data (a
                          dictionary) to filter the list of returned
                          usages.
        :param hints: An optional list of hints indicating which
                      attributes of the model will be required by the
                      calling code.  Only those attributes which
                      reference other fields need be listed, although
                      it is not an error to list other fields.  It is
                      also permissible to indicate deeper levels of
                      access by separating attributes with periods.
                      (In the case of reference fields which are
                      represented as lists, there is no need to use
                      square brackets.)

        :returns: A list of instances of ``boson.db.models.Usage``.
        """

        pass

    def create_quota(self, context, resource, auth_data, limit=None):
        """
        Create a new quota for a given resource and user.  Raises a
        Duplicate exception in the event that the new usage is a
        duplicate of an existing quota.

        :param context: The current context for accessing the
                        database.
        :param resource: The resource the quota is for.  Can be either
                         a ``Resource`` object or a UUID of an
                         existing resource.
        :param auth_data: Authentication and authorization data (a
                          dictionary).  This is used to match up a
                          quota with a particular user of the system.
        :param limit: The limit on the number of the resource that the
                      user is permitted to allocate.  Defaults to
                      ``None`` (unlimited).

        :returns: An instance of ``boson.db.models.Quota``.
        """

        pass

    def get_quota(self, context, id=None, resource=None, auth_data=None,
                  hints=None):
        """
        Look up a specific quota by id or by resource and
        authentication and authorization data.

        :param context: The current context for accessing the
                        database.
        :param id: The ID of the quota to look up.
        :param resource: The ``Resource`` or resource ID of the
                         resource to look up the quota for.
        :param auth_data: Authentication and authorization data (a
                          dictionary).
        :param hints: An optional list of hints indicating which
                      attributes of the model will be required by the
                      calling code.  Only those attributes which
                      reference other fields need be listed, although
                      it is not an error to list other fields.  It is
                      also permissible to indicate deeper levels of
                      access by separating attributes with periods.
                      (In the case of reference fields which are
                      represented as lists, there is no need to use
                      square brackets.)

        Note: either provide ``id`` or both ``resource`` and
        ``auth_data``.  If an invalid combination of arguments is
        provided, a TypeError will be raised.  If no matching resource
        can be found, a KeyError will be raised.

        :returns: An instance of ``boson.db.models.Quota``.
        """

        pass

    def get_quotas(self, context, resource=None, auth_data=None, hints=None):
        """
        Retrieve a list of all defined quotas.

        :param context: The current context for accessing the
                        database.
        :param resource: A ``Service`` or service ID to filter the
                         list of returned quotas.
        :param auth_data: Authentication and authorization data (a
                          dictionary) to filter the list of returned
                          quotas.
        :param hints: An optional list of hints indicating which
                      attributes of the model will be required by the
                      calling code.  Only those attributes which
                      reference other fields need be listed, although
                      it is not an error to list other fields.  It is
                      also permissible to indicate deeper levels of
                      access by separating attributes with periods.
                      (In the case of reference fields which are
                      represented as lists, there is no need to use
                      square brackets.)

        :returns: A list of instances of ``boson.db.models.Quota``.
        """

        pass

    def create_reservation(self, context, expire):
        """
        Create a new reservation.

        :param context: The current context for accessing the
                        database.
        :param expire: A date and time at which the reservation will
                       expire.

        :returns: An instance of ``boson.db.models.Reservation``.
        """

        pass

    def reserve(self, context, reservation, resource, usage, delta):
        """
        Reserve a particular amount of a specific resource.

        :param context: The current context for accessing the
                        database.
        :param reservation: The reservation the item is reserved in.
                            Can be either a ``Reservation`` object or
                            a UUID of an existing reservation.
        :param resource: The resource the reserved item is for.  Can
                         be either a ``Resource`` object or a UUID of
                         an existing resource.
        :param usage: The usage record for the resource reservation.
                      Can be either a ``Usage`` object or a UUID of an
                      existing usage.
        :param delta: The amount of the resource to reserve.  May be
                      negative for deallocation.

        :returns: An instance of ``boson.db.models.ReservedItem``.
        """

        pass

    def get_reservation(self, context, id, hints=None):
        """
        Look up a specific reservation by id.

        :param context: The current context for accessing the
                        database.
        :param id: The ID of the reservation to look up.
        :param hints: An optional list of hints indicating which
                      attributes of the model will be required by the
                      calling code.  Only those attributes which
                      reference other fields need be listed, although
                      it is not an error to list other fields.  It is
                      also permissible to indicate deeper levels of
                      access by separating attributes with periods.
                      (In the case of reference fields which are
                      represented as lists, there is no need to use
                      square brackets.)

        Note: if no matching reservation can be found, a KeyError will
        be raised.

        :returns: An instance of ``boson.db.models.Reservation``.
        """

        pass

    def expire_reservations(self, context):
        """
        Rolls back all expired reservations.

        :param context: The current context for accessing the
                        database.
        """

        pass

    def _lazy_get(self, context, base_obj, field, hints, klass):
        """
        Called to obtain the given field from the base database
        object.  Used to resolve cross-references to other database
        objects.

        :param context: The current context for accessing the
                        database.
        :param base_obj: The underlying database object to retrieve
                         the field from.
        :param field: The name of the field to retrieve.
        :param hints: An object expressing hints to the underlying
                      database system.  This object will have been
                      passed to the model class constructor by the
                      underlying database system.
        :param klass: The model class that is expected to be returned
                      from ``lazy_get()``.

        :returns: An instance of ``klass``.
        """

        pass

    def _lazy_get_list(self, context, base_obj, field, hints, klass):
        """
        Called to obtain the given field from the base database
        object.  Used to resolve cross-references to lists of other
        database objects.

        :param context: The current context for accessing the
                        database.
        :param base_obj: The underlying database object to retrieve
                         the field from.
        :param field: The name of the field to retrieve.
        :param hints: An object expressing hints to the underlying
                      database system.  This object will have been
                      passed to the model class constructor by the
                      underlying database system.
        :param klass: The model class that is expected to be returned
                      from ``lazy_get_list()``.

        :returns: A list of instances of ``klass``.
        """

        pass

    def _save(self, context, base_obj):
        """
        Called to update the underlying database with the changes made
        to a base database object.

        :param context: The current context for accessing the
                        database.
        :param base_obj: The underlying database object to save to the
                         database.
        """

        pass

    def _delete(self, context, base_obj):
        """
        Called to delete the underlying base database object from the
        database.

        :param context: The current context for accessing the
                        database.
        :param base_obj: The underlying database object to delete from
                         the database.
        """

        pass
